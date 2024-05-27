from functionspge import *
import sys

logindetails = [
    {"username": "Yaw", "password": "Idey4You"},
    {"username": "User1", "password": "12345"}
]

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
            signloop = 2  # Set signloop to break the outer loop
            T = 2  # Set T to break the inner loop

        else:
            print("Wrong Input!")
            T = 2  # Set T to break the inner loop

    # Reset T and signloop for the next iteration of the outer loop
    T = 0
    signloop = 0

    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # Flag variable to track if a matching user was found
    user_found = False

    for user in logindetails:
        if user["username"] == username and user["password"] == password:
            print("Access granted")
            user_found = True  # Set the flag
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
                        makeReserve(loc)
                        j = 2

                elif opt == "3":
                    print("1. Load Reservation Receipt Data")
                    print("2. Load Location Data")
                    print("3. Main Menu")
                    print("4. Exit")
                    count=0
                    savecount=0
                    while savecount<1:
                        sub_opt= input("Please input an Option : ")
                        if sub_opt == "1":
                            with open("Receipt.txt", "r") as file:
                                content = file.read()
                                print(content)
                                        
                        elif sub_opt =="2":
                            loc=[]
                            current_location = {}
                            loc.clear()
                            with open("locations.txt","r") as file:
                                current_location = {}
                                for line in file:
                                    if line.strip():
                                        key, value = line.strip().split(": ")
                                        current_location[key] = value
                                    else:
                                        loc.append(current_location)
                                        current_location = {}
                                if current_location:
                                    loc.append(current_location)
                                print("Reconstructed list of dictionaries:")
                                print(loc)
                        elif sub_opt=="3":
                            savecount= 2
                        elif sub_opt =="4":
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
