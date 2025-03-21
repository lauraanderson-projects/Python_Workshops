def show_homepage():
    print("") 
    print("          === DonateMe Homepage ===          ")
    print("---------------------------------------------")
    print("| 1.    Login       | 2.    Register        |")
    print("---------------------------------------------")
    print("| 3.    Donate      | 4.    Show Donations  |")
    print("---------------------------------------------")
    print("|              5.   Exit                    |")	
    print("---------------------------------------------")
    
def donate(username):
    donation_amt = input(f"\n{username}, enter your donation amount: ")
    donation_string = f"{username} donated ${donation_amt}"
    print("Thank you for your donation!")
    return donation_string  # Return the donation string for further processing