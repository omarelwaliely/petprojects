import csv
from faker import Faker
from datetime import date
import random

emails = []
usernames = []
brands = ['Kia', 'Alfa Romeo', 'Chery', 'Lada', 'Faw', 'Isuzu', 'Jaguar', 'Chevrolet', 'Daewoo', 'Rolls Royce', 'Honda', 'Brilliance', 'Dodge', 'Changan', 'Peugeot', 'Jac', 'Volvo', 'Jetour', 'Renault', 'Mazda', 'GMC', 'Opel', 'Fiat', 'Geely', 'Ssang Yong', 'Baic', 'Cadillac', 'Other make', 'Lamborghini', 'Maserati', 'Mitsubishi', 'BMW', 'Lifan', 'Audi', 'Nissan', 'Senova', 'Infiniti', 'Tesla', 'Citroen', 'Skoda', 'Zotye', 'King Long', 'Chrysler', 'Bentley', 'Changhe', 'Bestune', 'Haval', 'Suzuki', 'BYD', 'Aston Martin', 'Porsche', 'Speranza', 'Jeep', 'Seat', 'Daihatsu', 'MG', 'Saipa', 'Toyota', 'DFSK', 'Proton', 'Hyundai', 'Mercedes-Benz', 'Subaru', 'Ford', 'Volkswagen', 'Land Rover', 'MINI']
models= ['TT', 'Convertible', 'RX5', 'S3', 'Tiggo', 'Hilux', 'Zaz', 'E200', 'Challenger', 'Waja', 'Jetta', 'CL-Class', 'Tucson', 'Wraith', 'Nubira', 'E63', 'A11', 'Eclipse', 'Grand Cherokee', 'Crossland', '3008', 'Lanos', 'Picanto', 'Gran Max', 'DS3', 'Flying Spur', 'Cerato Coupe', 'Xceed', 'CR-V', 'Fiesta', 'Fusion', 'Cerato', 'Preve', 'Tivoli XLV', 'Evoque', '128', 'Camry', 'Ibiza', 'Explosion', '21', 'Ram', 'Cooper Paceman', 'Grand Terios', 'Emgrand X7', '418', 'Edge', 'Captur', 'Town and Country', 'Materia', 'Granta', 'Elantra', 'GLC 300', 'Camaro', 'Pickup', 'Van', 'S7', '530', 'Range Rover Vogue', 'Tiida', 'Durango', 'Tiba', 'Kuga', '520', '535', 'Golf', 'Saga', 'Auris', 'S-Presso', 'Rav 4', 'Panamera', '218', 'Pickup/Dababa', 'Tivoli', '740', 'C5', 'Santa Fe', 'Fortuner', 'A7', 'Sonic', 'X1', 'Insignia', 'A200', 'Giulia', 'Okavango', 'Alsvin', 'QQ', '330', 'E250', 'GLK 300', 'Model X', 'DFM', 'S450', 'H6', 'C4 Picasso', 'S500', 'CLA 200', 'Rio', '6', 'Ghibli', 'E350', 'B180', 'JS4', 'X70', 'I20', 'Bluebird', 'Windstar', 'C-HR', 'Leganza', '316', 'Pacifica', 'X3', 'A113', 'S400', 'Belta', 'Accord', 'A180', 'Armada', 'A1', 'X7', 'Bayon', 'Yukon', 'XF', 'Eagle 580', 'Sephia', 'F-type', '208', 'X30', 'Ertiga', 'Sorento', 'Leon', 'Velar', 'Civic', 'Q8', 'Clio', 'D-Max', 'GLS', 'Liberty', 'FRV Cross', 'X35', 'Compass', 'Mahindra', 'Countryman S', 'Ghost', 'Logan', 'E280', 'Prado', 'Defender', 'E180', 'CLA 180', 'Spark', 'XC60', 'F0', 'M11', 'Sandero', 'Arrizo 5', 'Bentayga', 'ID4', 'DS5', 'I10', 'Outlander', 'H1', 'Jolion', 'Malibu', 'Wrangler', 'FRV', 'Juliet', 'C4 Grand Picasso', 'IX35', 'Impreza', 'Cherokee', 'Pride', 'Verna', 'Doblo', '2008', 'B200', '607', 'Coupe', 'Astra', 'Siena', '405', 'F-Pace', 'X4', 'Emgrand 7', '2110', '3', 'Sebring', '207', 'X-Trail', 'Gen-2', 'Passat', 'E240', 'Toledo', 'Creta', 'Linea', 'Rapid', '528', 'Kodiaq', 'GLA 200', 'Scala', 'Terios', 'Ceed', 'Cruze', 'Punto', 'Getz', 'X2', 'Discovery', 'Sandero Stepway', 'C280', 'Megane', 'X95', 'QX', 'Continental', 'CC', 'C240', 'X5', 'Range Rover Sport', 'Escalade', 'Pandido', '500X', '301', 'Z4', 'Commander', 'Vectra', 'Pick up', 'EADO', 'Other', 'J7', 'Vitara', 'Alto', 'Cordoba', 'GLC 250', 'C200', 'Qashqai', 'Xpander', 'Avanza', 'Scenic', 'Super Panda', '850', 'V5', 'Fluence', 'A3', 'City', 'Echo', 'Swift', 'Duster', 'Countryman', 'X6', '750', 'Matrix', 'JS3', 'Solaris', 'Corolla', 'Mustang', 'Cooper s', 'Rush', 'E230', 'S560', 'XV', 'T55', 'Veloster', 'Grand Punto', 'Santamo', 'Yaris', 'Charade', 'A516', 'Rumion', 'Ateca', 'Ciaz', 'Foton', 'Jumpy', 'A8', 'Grandland', 'Range Rover', 'Roomster', 'LR3', 'Palio', 'E300', '307 SW', 'Q2', 'Arona', 'GLE-Class', 'XE', 'Previa', 'C3 Picasso', 'Renegade', 'E220', 'G-Class', 'T600', 'DS7', '340', 'PT Cruiser', 'MG 5', 'Clubman', 'CLS', 'C3', 'Tarraco', 'Jinbei', 'B150', 'Superb', 'ZS', 's60', 'Ka', 'Symbol', 'Lacetti', '2106', 'Q5', 'N300', 'Dart', 'GLK 250', '2107', 'Juke', 'Carnival', 'Q7', 'Maruti', 'Corsa', 'Focus', 'Shahin', 'Tipo', 'V7', '307', 'GL-Class', 'Cooper Roadster', 'MG 750', '508', 'L3', 'C300', 'Maybach', 'Boxster', 'Shuma', 'Kancil', 'GLC 200', 'Landwind', 'Glory 330', 'Kamiq', 'Captiva', 'A620', 'Cascada', 'S2', 'C4', 'Legacy', 'Sonata', 'Mokka', 'C230', '5008', 'Petra', 'F3', 'XC90', 'Octavia', 'GT-R', '308 SW', 'Jazz', '523', 'Polo', 'Pajero', 'Cayenne', 'SX4', 'Karoq', 'Sentra', 'Lancer', '118', '318', 'Xsara', 'Soul', 'Pegas', 'Carens', 'Caddy', '500', 'Aveo', 'Benni mini', 'S350', 'Meriva', 'Model 3', 'Giulietta', 'Range Rover Sport SVR', 'Sportage', 'C180', 'Charger', 'N200', 'A150', 'A6', 'Carrera', 'Model Y', 'Dzire', '525', '335', 'Avante', 'C-Elysée', 'H530', '406', 'Rapide S', 'Q', 'Land Cruiser', 'A4', 'E-Pace', 'HS', 'Jimny', 'Galena', 'Sierra', 'Sunny', '320', 'Stelvio', '328', '116', '911', 'Accent', 'Envy', 'Grand I10', '630', 'Optra', 'Corvette', 'C250', 'Bravo', 'A5', 'SLC-Class', '407', 'GranTurismo', '640', 'Cooper', 'FSV', 'Kadjar', 'Tiguan', 'Macan', 'Q3', 'Trailblazer', 'Expedition']
car_brand_row = []
car_model_row = []

fake = Faker()
usernames = []
emails = []
with open('users.csv', mode='w', newline='') as csv_file:
    fieldnames = ['gender', 'age', 'birthdate', 'username', 'email']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1000):
        profile = fake.profile()
        birthdate = profile['birthdate']
        age = date.today().year - birthdate.year - ((date.today().month, date.today().day) < (birthdate.month, birthdate.day))
        while age > 100 or age < 18 or  profile['username']in usernames or  profile['mail'] in emails:
            profile = fake.profile()
            birthdate = profile['birthdate']
            age = date.today().year - birthdate.year - ((date.today().month, date.today().day) < (birthdate.month, birthdate.day))
        email = profile['mail']
        username = profile['username']
        emails.append(email)
        usernames.append(username)
        gender = profile['sex']
        writer.writerow({
            'gender': gender,
            'age': age,
            'birthdate': birthdate.strftime('%Y-%m-%d'),
            'username': username,
            'email': email
        })
csv_file.close()
with open('car_models.csv', mode='w', newline='') as csv_file:
    fieldnames = ['username', 'car_model']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1000):
        car_model = random.choice(models)
        username = random.choice(usernames)
        while (car_model, username) in car_model_row:
            car_model = random.choice(models)
            username = random.choice(usernames)
        car_model_row.append((car_model, username))
        writer.writerow({
            'car_model': car_model,
            'username': username
        })
csv_file.close()
with open('car_brands.csv', mode='w', newline='') as csv_file:
    fieldnames = ['username', 'car_brand']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(1000):
        car_brand = random.choice(brands)
        username = random.choice(usernames)
        while (car_brand, username) in car_brand_row:
            car_brand = random.choice(brands)
            username = random.choice(usernames)
        car_brand_row.append((car_brand, username))
        writer.writerow({
            'car_brand': car_brand,
            'username': username
        })
csv_file.close()

used = []
with open('review.csv', mode='w', newline='') as csvfile, open('ad.csv', mode='r') as adfile:
    ad_reader = csv.reader(adfile)
    next(ad_reader)
    ads = list(ad_reader)
    fieldnames = ['textreview', 'rating', 'adid', 'username','price']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in range(100):
        username = random.choice(usernames)
        rating = random.randint(1, 5)
        textreview = fake.paragraph(nb_sentences=3)
        adid = random.choice(ads)[0]
        price = random.choice(ads)[4]
        while adid in used:
            adid = random.choice(ads)[0]
            price = random.choice(ads)[4]
        used.append(adid)
        writer.writerow({
            'price': price,
            'textreview': textreview,
            'rating': rating,
            'adid': adid,
            'username': username
        })
csvfile.close()


    

#code to take out all unique values so i can put them in the arrays at the top (once with 'brand' once with 'model')
#unique_values = set()
# with open('olx.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         unique_values.add(row['brand'])

# print(unique_values)