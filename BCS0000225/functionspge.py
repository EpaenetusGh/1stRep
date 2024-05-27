loc=[
    {"Location_name": "South Beach", "city": "Tokyo", "country": "Japan", "Price Per Person": 100, "Price Per 2 Persons": 300, "Discount": 0.20},
    {"Location_name": "Big Apple", "city": "New York City", "country": "USA", "Price Per Person": 200, "Price Per 2 Persons": 500, "Discount": 0.20},
    {"Location_name": "Big Ben", "city": "London", "country": "UK", "Price Per Person": 100, "Price Per 2 Persons": 150, "Discount": 0.10}
]


loccount= len(loc)
from datetime import datetime


def add_loc(location_name,city,country,ppp,pp2p,discount):
    global loc
    loc_info = {"Location_name": location_name, "city": city, "country": country, "Price Per Person":  ppp, "Price Per 2 Persons": pp2p, "Discount": discount }
    loc.append(loc_info)
    global loccount
    loccount = len(loc)
    with open('locations.txt', 'a') as file:
        file.write(f"Location_name: {location_name}\n")
        file.write(f"City: {city}\n")
        file.write(f"Country: {country}\n")
        file.write(f"Price per person: {ppp}\n")
        file.write(f"Price per 2 people: {pp2p}\n")
        file.write(f"Discount Price available: {discount}\n\n")
    print("Location added successfully")

def displayloc():
    headings=["Location |", "City |" , " Country   |" , "Price Per Person|" , "Price Per 2 Persons  |" , "Discount in percentage(%) where 1 is 100% Discount & 0 is 0% Discount"]
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(*headings))
    print("-" * 110)
    for location in loc:
        print("{:<15} {:<15} {:<15} {:<20} {:<20} {:<20}" .format(
            location.get('Location_name'," "),
            location.get('city'," "),
            location.get('country'," "),
            location.get('Price Per Person'," "),
            location.get('Price Per 2 Persons'," "),
            location.get('Discount', " ")
            ))
    with open('locations.txt', 'w') as file:
        for location in loc:
            file.write(f"Location_name: {location.get('Location_name', '')}\n")
            file.write(f"City: {location.get('city', '')}\n")
            file.write(f"Price per person: {location.get('Price Per Person', '')}\n")
            file.write(f"Price per 2 people: {location.get('Price Per 2 Persons', '')}\n")
            file.write(f"Discount: {location.get('Discount', '')}\n\n")    

def remove_loc(location_name, city, country):
    global loc
    global loccount
    
    for location in loc:
        if (location.get("Location_name") == location_name and
            location.get("city") == city and
            location.get("country") == country):
            loc.remove(location)
            loccount = len(loc)
            print(f"Place {location_name}, {city}, {country} removed successfully.")
            return
    
    print(f"No place with name {location_name}, city {city}, and country {country} found.")


def menu():
    print("Welcome to LaVie Transport and Tours")
    print("Please choose an option: ")
    print("1. Location.")
    print("2. Reservation.")
    print("3. Save Data.")
    print("4. Exit.")

def loc_menu():
    print("Locations Count", loccount)
    print("1. Add New Location")
    print("2. Remove Location")
    print("3. Back")
    print("4. Exit")

def res_menu():
    print("1. Number per rooms")
    print("2. Number of rooms")
    print("3. Choose Location")
    print("3. Exit")
    print("4. Total Cost")

def locchoice():
    print("")

def Reserveinfo(rname,rtel,ctime,pepnum,roomnum):
    ctime=datetime.now().time()
    reservation = {
        "Name": rname,
        "Phone Number": rtel,
        "Time": ctime,
        "People Per Room": pepnum,
        "Number of Rooms": roomnum
    }
    return reservation

def print_receipt(rname, rtel, locationname, cityname, countryname, room1p, room2p, net_price):
    print("\n--- Receipt ---")
    print("Customer Name : ", rname)
    print("Customer Contact : ", rtel)
    print("Location Name : ", locationname)
    print("City : ", cityname)
    print("Country : ", countryname)
    print("One Person Rooms requested : ", room1p)
    print("Two Persons Rooms requested : ", room2p)
    print("Your final cost will be GHc ", net_price)
    print("Thank You for choosing LaVie Transport and Tours !")
    print("")
    print("")


def makeReserve(loc):
    rname = input("Kindly Input your Name: ")
    rtel = input("Kindly Input your Phone Number(Do not add the 0): ")
    rtel = "+233" + rtel
    ctime=datetime.now().time()
    locationname= input("Enter the Name of the location: ")
    cityname=input("Enter the name of the city: ")
    countryname= input("Enter the name of the country: ")
    

    print("Welcome ! ", rname)

    for location in loc:
        if location["Location_name"] == locationname and location["city"]== cityname and location["country"]== countryname:
            print("Location Found")
            room1p=int(input("Enter the number of rooms for 1 person: " ))
            room2p=int(input("Enter the number of rooms for 2 people: " ))

            total= (room1p *location["Price Per Person"]) + (room2p * location["Price Per 2 Persons"])
            discountp= total * location["Discount"]
            netprice=total - discountp

            print("\n--- Receipt ---")
            print("Customer Name : ", rname)
            print("Customer Contact : ", rtel)
            print("Location Name : ", locationname)
            print("City : ",cityname )
            print("Country : ", countryname)
            print("One Person Rooms requested : ", room1p)
            print("Two Persons  Rooms requested : ", room2p)
            print("Your final cost will be GHc " , netprice)
            print("")
            print("Time of Receipt : ", ctime)
            print("Thank You for choosing LaVie Transport and Tours !")
            print("")
            print("")

            with open("Receipt.txt", "a") as file:
                file.write("")
                file.write("\n--- Receipt ---\n")
                file.write("")
                file.write("Customer Name : " + rname + "\n")
                file.write("Customer Contact : " + rtel + "\n")
                file.write("Location Name : " + locationname + "\n")
                file.write("City : " + cityname + "\n")
                file.write("Country : " + countryname + "\n")
                file.write("One Person Rooms requested : " + str(room1p) + "\n")
                file.write("Two Persons  Rooms requested : " + str(room2p) + "\n")
                file.write("Your final cost will be GHc " + str(netprice) + "\n\n")
                file.write("\nTime of Receipt : " + str(ctime) + "\n")
                file.write("")
                file.write("Thank You for choosing LaVie Transport and Tours !\n\n")
            return netprice
    print("Location not found")
    return None

reservations = [] 

def Reserveinfo(rname,rtel,ctime,pepnum,roomnum):
    ctime=datetime.now().time()
    reservation = {
        "Name": rname,
        "Phone Number": rtel,
        "Time": ctime,
        "People Per Room": pepnum,
        "Number of Rooms": roomnum
    }
    global reservations
    reservations.append(reservation)
    return reservation


