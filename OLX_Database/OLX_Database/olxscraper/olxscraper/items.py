# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OlxscraperItem(scrapy.Item):
    phone = scrapy.Field()
    description = scrapy.Field()
    adid = scrapy.Field()
    location = scrapy.Field()
    addate = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    model = scrapy.Field()
    fueltype = scrapy.Field()
    price = scrapy.Field()
    pricetype = scrapy.Field()
    paymentoptions = scrapy.Field()
    year = scrapy.Field()
    kilometers_begin = scrapy.Field()
    kilometers_end = scrapy.Field()
    color = scrapy.Field()
    transmission = scrapy.Field()
    bodytype = scrapy.Field()
    enginecap_start = scrapy.Field()
    enginecap_end = scrapy.Field()
    features = scrapy.Field()
    sellerfname = scrapy.Field()
    sellerlname = scrapy.Field()
    phonenumbers = scrapy.Field()
    commercialid = scrapy.Field()
    joindate = scrapy.Field()
    profileurl = scrapy.Field()
    pass
