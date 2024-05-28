from functionspge import *
import sys

logindetails = [
    {"username": "Yaw", "password": "Idey4You"},
    {"username": "User1", "password": "12345"},
    {"username": "1","password":"1"}
]

# Load locations from file at the start
load_locations_from_file()

logloop = 0
while logloop < 1:
    print("Welcome To LaVie Travel & Tours.")
    print("Are you a New User?")
    signup = input("1. Yes\n2. No\n")

    signloop = 0
    T = 0
    while signloop < 1:
        if signup == "1":
            while T < 1:
                nusername = input("Enter Your Desired Username: ")
                nuserpass = input("Enter Your Desired Password: ")
                username_exists = any(user["username"] == nusername for user in logindetails)
                if username_exists:
                    print("Username already exists. Please choose a different username.")
                else:
                    logindetails.append({"username": nusername, "password": nuserpass})
                    print("User Added Successfully")
                    T = 2  
            signloop = 2  

        elif signup == "2":
            print("Welcome Back")
            signloop = 2  
            T = 2  

        else:
            print("Wrong Input!")
            T = 2  

    T = 0
    signloop = 0

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    user_found = False

    for user in logindetails:
        if user["username"] == username and user["password"] == password:
            print("Access granted")
            user_found = True  
            count = 0
            while count < 1:
                menu()
                opt = input("Please choose an option: ")

                if opt == "1":
                    lcount = 0
                    while lcount < 1:
                        displayloc()
                        loc_menu()
                        choice = input("Please choose an option: ")
                        if choice == "1":
                            place_name = input("Enter the name of the place: ")
                            city = input("Enter the city of the place: ")
                            country = input("Enter the country of the place: ")
                            ppp = int(input("What is the Price per person? "))
                            pp2p = int(input("What is the Price per 2 people? "))
                            discount = float(input("Discount Price available: "))
                            add_loc(place_name, city, country, ppp, pp2p, discount)

                        elif choice == "2":
                            location_name = input("Enter the name of the place: ")
                            city = input("Enter the city of the place: ")
                            country = input("Enter the country of the place: ")
                            remove_loc(location_name, city, country)

                        elif choice == "3":
                            lcount = 2

                        elif choice == "4":
                            print("Thank You for contacting LaVie Travels and Tour")
                            lcount = 2
                            count = 2
                            sys.exit()

                elif opt == "2":
                    j = 0
                    while j < 1:
                        displayloc()
                        makeReserve()
                        j = 2

                elif opt == "3":
                    print("1. Load Reservation Receipt Data")
                    print("2. Load Location Data")
                    print("3. Main Menu")
                    print("4. Exit")
                    savecount = 0
                    while savecount < 1:
                        sub_opt = input("Please input an Option: ")
                        if sub_opt == "1":
                            try:
                                with open("Receipt.txt", "r") as file:
                                    content = file.read()
                                    print(content)
                            except FileNotFoundError:
                                print("Receipt.txt not found.")
                                        
                        elif sub_opt == "2":
                            load_locations_from_file()
                            print("Reconstructed list of dictionaries:")
                            print(loc)

                        elif sub_opt == "3":
                            savecount = 2

                        elif sub_opt == "4":
                            print("Exiting...")
                            sys.exit()

                elif opt == "4":
                    print("Exiting the system... Thank You!")
                    sys.exit()
                else:
                    print("Incorrect Input")
                    break

            break  

    if not user_found:
        print("Incorrect Username or Password")
        logloop = 2
