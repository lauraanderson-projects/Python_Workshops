from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"admin": "password123",}  # Example user database

donations = []  # List to store donations

authorized_user = ""

# Main loop to show the homepage and handle user input

while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate.")
    else:
        print(f'You can now make a donation.')
    
    option = input("Enter an option: ")
    
    if option == "1":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
        continue
    elif option == "2":
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username, password)
        if authorized_user != "":
            database[username] = password  # Add the new user to the database
        continue
    elif option == "3":
        if authorized_user == "":
            print("You must be logged in to donate.")
            continue
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)  # Store the donation string in the donations list
        continue
    elif option == "4":
        show_donations(donations)
        continue
    elif option == "5":
        print("Exiting the application. Goodbye!")
        break