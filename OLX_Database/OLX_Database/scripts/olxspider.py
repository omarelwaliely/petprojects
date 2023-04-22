import scrapy
import re
import json
from csv import writer
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from olxscraper import items

count = 1
cookies = {}
item = items.OlxscraperItem()
class OlxspiderSpider(scrapy.Spider):
    
    name = "olxspider"
    allowed_domains = ["www.olx.com.eg"]
    start_urls = ["https://www.olx.com.eg/en/vehicles/cars-for-sale/cairo/?filter=new_used_eq_2%2Cyear_between_2000_to_2023"]
                
    def parse(self, response):
        global count
        with open('cookies.txt', 'r') as f:
         cookie_json = json.load(f)
        for link in response.css('li.c46f3bfe a::attr(href)'): # no prefix
            newlink = 'https://www.olx.com.eg' + link.get()
            yield response.follow(link.get(),callback = self.parsePage)
        count = count+1
        yield scrapy.Request(f'https://www.olx.com.eg/en/vehicles/cars-for-sale/cairo/?page={count}&filter=new_used_eq_2%2Cyear_between_2000_to_2023',callback = self.parse,cookies = cookie_json)
        

    def parsePage(self,response):
        url = response.url
        item = items.OlxscraperItem()
        pattern = r"ID(\d+)\.html"
        match = re.search(pattern, url)
        if match:
            adid = match.group(1)
        else:
            adid = 'CHECKFORERROR'
        
        #adid = response.css('div._171225da ::text').get()[6:]
        prev,memtime,comid,features,brand,model,fuel,ptype,year,kmstart,kmend,transmission,poption,fname,lname, color,btype,ecstart, ecend, plink= '','','','', '' , '','','','','','','','','','','','','','',''
        if response.selector.xpath('//*[@id="body-wrapper"]/div[1]/header[2]/div/div/div/div[4]/div[2]/div[1]/div/div[2]/span[1]/text()').get() is None:
            location = ''
        else:
            location = response.selector.xpath('//*[@id="body-wrapper"]/div[1]/header[2]/div/div/div/div[4]/div[2]/div[1]/div/div[2]/span[1]/text()').get().replace(', Cairo', '')
        datecheck = response.selector.xpath('//*[@id="body-wrapper"]/div/header[2]/div/div/div/div[4]/div[2]/div[1]/div/div[2]/span[2]/span/text()').get()
        if 'day' in datecheck:
            adddate =datetime.today() - timedelta(days = int(datecheck.replace(' days ago','').replace(' day ago','')))
        elif 'months' in datecheck:
            return
        elif 'month' in datecheck:
            adddate =datetime.today() - relativedelta(months = int(datecheck.replace(' month ago','')))
        elif 'year' in datecheck:
            adddate =datetime.today() - relativedelta(years = int(datecheck.replace(' years ago','').replace(' year ago','')))
        elif 'week' in datecheck:
            adddate =datetime.today() - relativedelta(weeks = int(datecheck.replace(' weeks ago','').replace(' week ago','')))
        else:
            adddate = datetime.today()
        for comormem in response.css('div.cf4781f0 span::text'):
            if'Member since' in comormem.get():
                memtime = comormem.get()[13:]
            if'Commercial ID:' in comormem.get():
                comid = comormem.get()[14:] 
        for feature in response.css('span._66b85548 ::text'):
            features = features + feature.get() + ';'
        features = features[:len(features)-1]
        for category in response.css("div.b44ca0b3 span::text"):
            if prev == 'Brand':
                brand = category.get()
            elif prev == 'Model':
                model = category.get()
            elif prev == 'Fuel Type':
                fuel = category.get()   
            elif prev == 'Price Type':
                ptype = category.get()   
            elif prev == 'Year':
                year = category.get()   
            elif prev == 'Kilometers':
                if 'More than ' in category.get():
                    kmstart = category.get().replace('More than ', '')
                    prev = category.get()
                    continue
                res = re.split(' to ',category.get())
                kmstart = res[0]
                kmend = res[1]
                res = '' 
            elif prev == 'Engine Capacity (CC)':
                if 'More than ' in category.get():
                    ecstart = category.get().replace('More than ', '')
                    prev = category.get()
                    continue
                if category.get() == '1600':
                    ecstart = '1600'
                    prev = category.get()
                    continue
                res = re.split(' - ',category.get())
                ecstart = res[0]
                ecend = res[1]
                res = '' 
            elif prev == 'Transmission Type':
                transmission = category.get()   
            elif prev == 'Payment Options':
                poption = category.get()   
            elif prev == 'Color':
                color = category.get()   
            elif prev == 'Body Type':
                btype = category.get()   
            prev = category.get()
        if fname == '': #had it like this to handle companies
            fname = response.selector.xpath('//*[@id="body-wrapper"]/div/header[2]/div/div/div/div[4]/div[2]/div[2]/div/a/div/div[2]/span/text()').get()
        description = response.css('div._0f86855a span::text').get()
        pnumbers = re.findall(r'(\+?2?0?\d{10})', description)
        pnumbers = [re.sub(r'^(\+?20|0)', '', number) for number in pnumbers]
        pnumbers = ';'.join(pnumbers)
        item['sellerfname'] = fname
        item['sellerlname'] =  lname
        item['phonenumbers'] =pnumbers
        item['commercialid'] = comid
        item['joindate'] = memtime,
        item['adid'] = adid
        item['location'] = location
        item['addate'] = adddate.strftime("%m-%d-%Y")
        item['title'] = response.css('h1.a38b8112 ::text').get()
        item['brand'] = brand
        item['model'] = model
        item['fueltype'] = fuel
        item['price'] = response.selector.xpath('//*[@id="body-wrapper"]/div/header[2]/div/div/div/div[4]/div[2]/div[1]/div/div[1]/div[1]/span/text()').get()[4:].replace(',','')
        item['pricetype'] = ptype
        item['paymentoptions'] = poption #might change
        item['year'] = year
        item['kilometers_begin'] = kmstart
        item['kilometers_end'] = kmend
        item['color'] = color
        item['transmission'] = transmission
        item['bodytype'] = btype
        item['enginecap_start'] = ecstart
        item['enginecap_end'] = ecend
        item['description'] = description
        item['features'] = features
        yield response.follow(f"https://www.olx.com.eg/api/listing/{adid}/contactInfo/",callback = self.getNumber,meta={
    'description': item['description'],
    'enginecap_start': item['enginecap_start'],
    'enginecap_end': item['enginecap_end'],
    'bodytype': item['bodytype'],
    'color': item['color'],
    'kilometers_begin': item['kilometers_begin'],
    'kilometers_end': item['kilometers_end'],
    'transmission': item['transmission'],
    'adid': item['adid'],
    'brand': item['brand'],
    'model': item['model'],
    'fueltype': item['fueltype'],
    'location': item['location'],
    'addate': item['addate'],
    'title': item['title'],
    'year': item['year'],
    'price': item['price'],
    'pricetype': item['pricetype'],
    'paymentoptions': item['paymentoptions'],
    'features': item['features'],
    'sellerfname': item['sellerfname'],
    'sellerlname': item['sellerlname'],
    'phonenumbers': item['phonenumbers'],
    'commercialid': item['commercialid'],
    'joindate': item['joindate'],
    })
        # yield{
        #     'profilelink': plink,
        #     'sellerfname': fname,
        #     'sellerlname': lname,
        #     'phonenumbers':pnumbers,
        #     'commercialid': comid,
        #     'joindate': memtime,
        #     'adid': adid,
        #     'location': location,
        #     'addate': adddate.strftime("%m-%d-%Y"),
        #     'title': response.css('h1.a38b8112 ::text').get(),
        #     'brand': brand,
        #     'model': model,
        #     'fueltype': fuel,
        #     'price': response.selector.xpath('//*[@id="body-wrapper"]/div/header[2]/div/div/div/div[4]/div[2]/div[1]/div/div[1]/div[1]/span/text()').get()[4:].replace(',',''),
        #     'pricetype': ptype,
        #     'paymentoptions': poption, #might change
        #     'year': year,
        #     'kilometers begin': kmstart,
        #     'kilometers end': kmend,
        #     'color': color,
        #     'transmission': transmission,
        #     'bodytype': btype,
        #     'enginecap start': ecstart,
        #     'enginecap end': ecend,
        #     'description': description,
        #     'features': features,
        # }
    def getNumber(self,response):
        item = items.OlxscraperItem()
        phone = ''
        for element in response.css('body'):
            phone_number_pattern = r'\+20(\d{10})'
            match = re.search(phone_number_pattern, element.get())
            if match:
                phone = match.group(1)
                break
            else:
                print(response.meta.get('adid') + 'BABABOOEY')
                return
        yield{
            'admin' : 'omar',
            'sellerfname': response.meta.get('sellerfname'),
            'phonenumbers':response.meta.get('phonenumbers'),
            'commercialid': response.meta.get('commercialid'),
            'joindate': response.meta.get('joindate'),
            'adid': response.meta.get('adid'),
            'location': response.meta.get('location'),
            'addate': response.meta.get('addate'),
            'title': response.meta.get('title'),
            'brand': response.meta.get('brand'),
            'model': response.meta.get('model'),
            'fueltype': response.meta.get('fueltype'),
            'price': response.meta.get('price'),
            'pricetype': response.meta.get('pricetype'),
            'paymentoptions': response.meta.get('paymentoptions'),
            'year': response.meta.get('year'),
            'kilometers begin': response.meta.get('kilometers_begin'),
            'kilometers end': response.meta.get('kilometers_end'),
            'color': response.meta.get('color'),
            'transmission': response.meta.get('transmission'),
            'bodytype': response.meta.get('bodytype'),
            'enginecapstart': response.meta.get('enginecap_start'),
            'enginecapend': response.meta.get('enginecap_end'),
            'description': response.meta.get('description'),
            'features': response.meta.get('features'),
            'phone' : phone
        }


    
