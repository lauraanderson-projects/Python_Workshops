from banking_pkg import account

def atm_menu(name):
    print("") 
    print("          === Automated Teller Machine ===          ")
    print(f'User:  {name.capitalize()}')
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")



balance = 0

name_to_validate = "laura"
pin_to_validate = "1234"


print("\n    === Automated Teller Machine ===    \n")
print("LOGIN")

while True:    
    try:
        name = input("Enter name to register: ")
        if len(name) <= 1 or len(name) >= 10:
            print("Invalid input. Please enter a valid user name length.")
            continue
        elif name == name_to_validate:
            break
        else:
            print("Incorrect information. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid user name.")

while True:
    try:
        pin = input("Enter PIN: ")
        if len(pin) < 4 or len(pin) > 4:
            print("Invalid input. Please enter a valid PIN length.")
            continue
        elif pin == pin_to_validate:
            print("\n*****Login successful!*****\n")
            break
        else:
            print("Incorrect information. Please try again.")
    except ValueError:
        print("Invalid input. numeric PIN.")

while True:
    atm_menu(name)
    option = input("Select an option: ")
    
    if option == '1':
        account.show_balance(balance)
    elif option == '2':
        balance = account.deposit(balance)
    elif option == '3':
        balance = account.withdraw(balance)
    elif option == '4':
        account.logout()
        break
    else:
        print("Invalid option. Please try again.")
        continue
