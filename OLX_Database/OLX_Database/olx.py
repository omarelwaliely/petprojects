import mysql.connector as sql
import re
import tabulate
import datetime

db = sql.connect(
    host="db4free.net",
    user="",
    password="", 
    database="olxdatabase"
)

def start():
    status = input("Welcome to OLX Scanner! Would you like to sign in, register, or exit? Enter 's', 'r', or 'e': ")
    if status.lower() == 's':
        signin()
    elif status.lower() == 'r':
        register()
    else:
        quit()

def signin():
    cursor = db.cursor()
    username = input("Input your existing Username: ")
    password = input("Input your Passsword: ")
    query = "SELECT * FROM appuser WHERE Username = '{}' AND password = '{}'".format(username, password)
    cursor.execute(query)
    pair = cursor.fetchone()
    
    if pair:
        print("Signed in Sucessfully.")
        menu(username)
    else:
        userchoice = input("Usename or Password is incorrect, try again, register, or exit? 't','r','e': ")
        if userchoice.lower() == 't':
            signin()
        elif userchoice.lower() == 'r':
            register()
        else:
            quit()

def preferences(username):
    try:
        cursor = db.cursor()
        carmake = input("Enter you car make preferences seperated by a comma: ")
        carmodel = input("Enter your car model preferences seperated by a comma: ")
        if carmake:
            carmake_list = [make.strip() for make in carmake.split(",")]
        else:
            carmake_list = []
        if carmodel:
            carmodel_list = [model.strip() for model in carmodel.split(",")]
        else:
            carmodel_list = []
            if carmake:
                for make in carmake_list:
                    query = "INSERT INTO userinterestmake (Make,Username) VALUES (%s,%s)"
                    values = (make,username,)
                    cursor.execute(query, values)
            if carmodel:
                for model in carmodel_list:
                    query = "INSERT INTO userinterestmodel (Model,Username) VALUES (%s,%s)"
                    values = (model,username)
                    cursor.execute(query, values)
        db.commit()
        menu(username)
    except:
        quit()
    
def register():
    cursor = db.cursor()
    print("REGISTER\n")
    username = input("Input a username: ")
    while(len(username)>30):
        username = input("Username must be less than 30 characters!, Input a username: ")
    while True:
        birthdate = input("Input a birthdate in the format YYYY-MM-DD: ")
        try:
            datetime.datetime.strptime(birthdate, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid format. Please enter a date in the format YYYY-MM-DD.")
    gender = input("Input your gender 'M' or 'F': ")
    while gender.upper() != 'M' and gender.upper()!='F' :
        print("That is not a valid input!")
        gender = input("Enter 'M' or 'F': ")
    email = input("Input your Email: ")
    while(len(email)>30):
        email = input("Email must be less than 50 characters!, Input an Email: ")
    bdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
    age = datetime.date.today().year - bdate.year - ((datetime.date.today().month, datetime.date.today().day) < (bdate.month, bdate.day))
    if(age <18):
        print("You are too young!")
        quit()
    while not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
        email = input("This is not a valid email make sure you have the format name@host.domain, try again: ")
    password = input('Input a password: ')
    while(len(password)>50):
        password = input("Password must be less than 50 characters!, Input a password: ")
    try:
        cursor.execute("INSERT INTO appuser (Gender, Age, Birth_Date, Username, Email_Address,password) VALUES (%s, %s,%s,%s, %s, %s)", (gender.upper(), age, birthdate,username,email,password))
        db.commit()
        
        print("Registered Succesfully.")
        preferences(username)
    except:
        trycase = input("That username or email already exists try again, sign in, or exit: 't', 's', or 'e': ")
        if trycase.lower() == 't':
            register()
        elif trycase.lower() == 's':
            signin()
        else:
            quit()

def menu(username):
    startuser = input("\n\nPREVIOUS WAS A SUCCESS AND EXECUTED ABOVE, would you like to continue or exit 'c' or 'e': ")
    if(startuser.lower() == 'e'):
        quit()
    userchoice = input("\n\nOLX SCANNER\n\nWould you like to: \n0. Add Preferences\n1. Add a new user sale for an ad\n2. View existing reviews of a given ad \n3. Get the aggregated rating of a seller\n4. Show all the ads for a given car make, body type and year in a specific location, along with the average price and the number of listings for each model\n5. Show all the used cars in a certain location in a given price range, with a given set of features\n6. Show the top 5 areas in cairo by amount of inventory and the average price given the make/model\n7. Show the top 5 sellers by the amount of listings they have, along with their average price per year\n8. Show all the cars listed by a specific owner\n9. Show the top 5 make/models by the amount of inventory and their average price for a given year range\n\nTYPE ANY OTHER NUMBER TO EXIT\n\nEnter a number: ")
    print("\n")
    if(userchoice =='1'):
        addSale(username)
    elif(userchoice =='0'):
        preferences(username)
    elif(userchoice == '2'):
        viewReviews(username)
    elif(userchoice =='3'):
        aggRating(username)
    elif(userchoice =='4'):
        carMakeBodyFind(username)
    elif(userchoice =='5'):
        locationPriceFeatures(username)
    elif(userchoice =='6'):
        topAreas(username)
    elif(userchoice =='7'):
        topSeller(username)
    elif(userchoice =='8'):
        ListedCars(username)
    elif(userchoice =='9'):
        topInventory(username)
    else:
        quit()
def allLocations():
    cursor = db.cursor()
    query = """
    SELECT DISTINCT adLocation from ad
    """
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid'))
    

def allMake():
    cursor = db.cursor()
    query = """
    SELECT DISTINCT Make from car
    """
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid'))
def allModel():
    cursor = db.cursor()
    query = """
    SELECT DISTINCT Model from car
    """
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid'))
def allBody():
    cursor = db.cursor()
    query = """
    SELECT DISTINCT BodyType from ad
    """
    cursor.execute(query)
    result = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid'))

def carMakeBodyFind(username):
    print("Here are all availiable locations: ")
    allLocations()
    location = input("Enter the location you want to search: ")
    print("Here are all availiable Makes: ")
    allMake()
    make = input("Enter the make you want to look for: ")
    print("Here are all availiable Body Types: ")
    allBody()
    body = input("Enter the body type you want to look for: ")
    year = input("Enter the year: ")
    cursor = db.cursor()
    query = """
    SELECT a.ID, a.Title, a.Descripton, a.AD_Date, subquery.Model, a.Color, a.StartCap, a.EndCap, a.StartOD, a.EndOD, a.FuelType, a.Poption, a.Price, a.Transmission, CAST(subquery.averageprice AS FLOAT) as Average_Price, subquery.numberlistings AS Listing_Count
    FROM (
        SELECT cl.Model, AVG(a.Price) as averageprice, COUNT(*) as numberlistings
        FROM carlisting cl 
        INNER JOIN ad a ON a.ID = cl.Listingid
        GROUP BY cl.Model
    ) subquery
    INNER JOIN carlisting cl ON cl.Model = subquery.Model
    INNER JOIN ad a ON cl.Listingid = a.ID
    WHERE LOWER(a.adLocation) = %s AND LOWER(cl.Make) = %s AND a.BodyType = %s AND cl.Car_Year = %s
    """
    param = (location.lower(),make.lower(),body,year)
    cursor.execute(query,param)
    result = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid',floatfmt=".2f"))
    menu(username)
def addSale(username):
    cursor = db.cursor()
    id = input("Enter the ADID for the car you bought: ")
    try:
        price = input("Enter the price you bought it for: ")
    except:
        print("INVALID: detected string starting over.")
        addSale(username)
    rating = input("How many stars do you rate this? (1-5): ")
    rating = int(rating)
    try:
        while(rating > 5 or rating < 1):
            rating = input("Please enter a valid rating!, (1-5): ")
            rating = int(rating)
    except:
        print("INVALID: detected string starting over.")
        addSale(username)
    review = input("Type up a review here: ")
    try:
        cursor.execute("INSERT INTO review (AD_ID, Price, Rating, Text_Review, Username) VALUES (%s, %s,%s,%s, %s)", (id, price, rating,review,username))
        db.commit()
        
        print("Review added.")
        menu(username)
    except:
        
        trycase = input("You have already created a review for this ad or the AD ID is not correct, try again or back to menu? 't', or 'm': ")
        if trycase.lower() == 't':
            addSale(username)
        else:
            menu(username)
def viewReviews(username):
    id = input("Enter the AD ID for the ad you want to check: ")
    cursor = db.cursor()
    query = """
    SELECT * 
    FROM review
    WHERE AD_ID = %s
    """
    param = (id,)
    cursor.execute(query,param)
    result = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid'))
    menu(username)

def aggRating(username):
    cursor = db.cursor()
    name = input("Enter a Seller's Full Name: ")
    phone = input("Enter a Seller's Phone Number: ")
    query = """
    SELECT a.sname,a.sphone, CAST(AVG(r.Rating) AS FLOAT) as Average_Rating
    FROM review r INNER JOIN ad a ON r.AD_ID = a.ID
    WHERE a.sname = %s AND a.sphone = %s
    GROUP BY 1,2;
    """
    params = (name,phone)
    try:
        cursor.execute(query,params)
        
        result = cursor.fetchall()
    except:
        
        print("ERROR: Make sure you put a value\n")
    headers = [desc[0] for desc in cursor.description]
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid',floatfmt=".2f"))
    menu(username)

def ListedCars(username):
    cursor = db.cursor()
    choice = input("Name, Phone, or Both? 'n','p',or 'b': ")
    if choice.lower() == 'n':
        name = input("Enter the Name: ")
        query = """
        SELECT c.Make,c.Model,c.Car_Year,a.Color,a.StartCap,a.EndCap,a.StartOD,a.EndOD,a.FuelType,a.Poption,a.Price,a.Transmission
        FROM ad a INNER JOIN
        carlisting c ON c.Listingid = a.ID 
        WHERE a.sname = %s
        """
        cursor.execute(query,(name,))
    elif choice.lower() == 'p':
        phone = input("Enter the Phone Number: ")
        query = """
        SELECT c.Make,c.Model,c.Car_Year,a.Color,a.StartCap,a.EndCap,a.StartOD,a.EndOD,a.FuelType,a.Poption,a.Price,a.Transmission
        FROM ad a INNER JOIN
        carlisting c ON c.Listingid = a.ID 
        WHERE a.sphone = %s
        """
        cursor.execute(query,(phone,))
    else:
        name = input("Enter the Name: ")
        phone = input("Enter the Phone Number: ")
        query = """
        SELECT c.Make,c.Model,c.Car_Year,a.Color,a.StartCap,a.EndCap,a.StartOD,a.EndOD,a.FuelType,a.Poption,a.Price,a.Transmission
        FROM ad a INNER JOIN
        carlisting c ON c.Listingid = a.ID 
        WHERE a.sname = %s AND a.sphone = %s
        """
        cursor.execute(query,(name,phone,))
    result = cursor.fetchall()

    headers = [desc[0] for desc in cursor.description]
    
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid',floatfmt=".2f"))
    menu(username)
def topAreas(username):
    cursor = db.cursor()
    choice = input("Type, Model, or Both? 't','m',or 'b': ")
    if choice.lower() == 't':
        print("Here are all the makes: ")
        allMake()
        make = input("Enter the Make: ")
        query = """
        SELECT a.adLocation, COUNT(*) as Amount, CAST(AVG(a.Price) as FLOAT) as Average_Price
        FROM ad a INNER JOIN carlisting cl ON a.ID = cl.Listingid
        WHERE cl.Make = %s
        GROUP BY 1
        ORDER BY 2 DESC,3 DESC
        limit 5;
        """
        cursor.execute(query,(make,))
    elif choice.lower() == 'm':
        print("Here are all the models: ")
        allModel()
        model = input("Enter the Model: ")
        query = """
        SELECT a.adLocation, COUNT(*) as Amount, CAST(AVG(a.Price) as FLOAT) as Average_Price
        FROM ad a INNER JOIN carlisting cl ON a.ID = cl.Listingid
        WHERE cl.Model = %s
        GROUP BY 1
        ORDER BY 2 DESC,3 DESC
        limit 5;
        """
        cursor.execute(query,(model,))
    else:
        print("Here are all the makes: ")
        allMake()
        make = input("Enter the Make: ")
        print("Here are all the models: ")
        allModel()
        model = input("Enter the Model: ")
        query = """
        SELECT a.adLocation, COUNT(*) as Amount, CAST(AVG(a.Price) as FLOAT) as Average_Price
        FROM ad a INNER JOIN carlisting cl ON a.ID = cl.Listingid
        WHERE cl.Make = %s AND cl.Model = %s
        GROUP BY 1
        ORDER BY 2 DESC,3 DESC
        limit 5;
        """
        cursor.execute(query,(make,model,))
    result = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid',floatfmt=".2f"))
    menu(username)
def topInventory(username):
    cursor = db.cursor()
    choice = input("Display Type, Model, or Both? 't','m',or 'b': ")
    range = input("Give a year range (ex: 2002-2005):  ")
    if(range):
        rangesplit = [ranges.strip() for ranges in range.split("-")]
        if(len(rangesplit[0])!=4 or len(rangesplit[1])!=4):
            print("INVALID: year must be of in format YYYY")
            topInventory(username)
    else:
        print("PLEASE ENTER VALUES!")
        topInventory(username)
    try:
        if choice.lower() == 't':
            query = """
            SELECT cl.Make, COUNT(*) as Amount, CAST(AVG(a.Price) AS FLOAT) as Average_Price
            FROM ad a INNER JOIN carlisting cl ON cl.Listingid = a.ID
            WHERE cl.Car_Year BETWEEN %s AND %s
            GROUP BY 1
            ORDER BY 2 DESC
            LIMIT 5;
            """
        elif choice.lower() == 'm':
            query = """
            SELECT cl.Model, COUNT(*) as Amount, CAST(AVG(a.Price) AS FLOAT) as Average_Price
            FROM ad a INNER JOIN carlisting cl ON cl.Listingid = a.ID
            WHERE cl.Car_Year BETWEEN %s AND %s
            GROUP BY 1
            ORDER BY 2 DESC
            LIMIT 5;
            """
        else:
            query = """
            SELECT cl.Make, cl.Model, COUNT(*) as Amount, CAST(AVG(a.Price) AS FLOAT) as Average_Price
            FROM ad a INNER JOIN carlisting cl ON cl.Listingid = a.ID
            WHERE cl.Car_Year BETWEEN %s AND %s
            GROUP BY 1, 2
            ORDER BY 2 DESC
            LIMIT 5;
            """
    except:
        print("INVALID: YEAR RANGE NOT CORRECT ex: type '2002-2010' without quotes try again!")
        topInventory(username)
    try:
        cursor.execute(query,(rangesplit[0],rangesplit[1],))
        
    except:
        
        print("INVALID: Make sure you put a range and that they are valid years ex: '2002-2010' without quotations")
        topInventory(username)
    result = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid',floatfmt=".2f"))
    menu(username)
def locationPriceFeatures(username):
    cursor = db.cursor()
    print("Here are all available locations:\n")
    allLocations()
    location = input("Enter a location: ")
    range = input("Give a price range (ex: 10000-200000):  ")
    if(range):
        rangesplit = [ranges.strip() for ranges in range.split("-")]
    else:
        print("PLEASE ENTER VALUES!")
        locationPriceFeatures(username)
    features = input("Give some features seperated by commas (ex: ABS,Air Conditioning):  ")
    if(features):
        featuresplit = [feature.strip() for feature in features.split(",")]
    else:
        print("PLEASE ENTER VALUES!")
        locationPriceFeatures(username)
    query = """
    SELECT cl.Make, cl.Model, cl.Car_Year, a.Color, a.StartCap, a.EndCap, a.StartOD, a.EndOD, a.FuelType, a.Poption, a.Price, a.Transmission
    FROM ad a
    INNER JOIN carlisting cl ON a.ID = cl.Listingid
    WHERE a.adLocation = %s AND a.Price BETWEEN %s AND %s AND
    (SELECT COUNT(*) FROM carfeatures cf
    WHERE cf.CarYear = cl.Car_Year AND cf.CarMake = cl.Make AND cf.CarModel = cl.Model AND cf.Feature IN ({features})) = %s;
    """.format(features=', '.join(['%s'] * len(featuresplit)))
    params = (location, rangesplit[0], rangesplit[1], *featuresplit, len(featuresplit))
    cursor.execute(query, params)
    result = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid',floatfmt=".2f"))
    menu(username)

def topSeller(username):
    cursor = db.cursor()
    #I interpreted this as average price per car year since there is only one month so only one year and the query would be useless
    query = """
    SELECT s1.FName, s1.Phone, s2.Listing_Amount, CAST(AVG(s1.OldAverage) AS FLOAT) as Average_Price_Annual
    FROM (
    SELECT s.FName, s.Phone, cl.Car_Year, AVG(a.Price) as OldAverage 
    FROM ad a 
    INNER JOIN carlisting cl ON cl.Listingid = a.ID 
    INNER JOIN seller s ON s.Fname = a.sname AND a.sphone = s.Phone
    GROUP BY 1,2,3
    ) s1
    INNER JOIN (
    SELECT s.FName, s.Phone, COUNT(*) as Listing_Amount
    FROM ad a 
    INNER JOIN carlisting cl ON cl.Listingid = a.ID 
    INNER JOIN seller s ON s.Fname = a.sname AND s.Phone = a.sphone
    GROUP BY 1,2
    ) s2 ON s1.FName = s2.FName AND s1.Phone = s2.Phone
    GROUP BY 1,2, s2.Listing_Amount
    ORDER BY s2.Listing_Amount DESC
    LIMIT 5;
    """
    cursor.execute(query)
    result = cursor.fetchall()
    
    headers = [desc[0] for desc in cursor.description]
    print(tabulate.tabulate(result, headers=headers, tablefmt='fancy_grid',floatfmt=".2f"))
    # for res in result:
    #     print(res)
    menu(username)


#menu('omarelwaliely')
#topSeller('omarelwaliely')
start()
