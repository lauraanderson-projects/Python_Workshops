class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
        
        #print(f'Name: {self.name}, Pin: {self.pin}, Password: {self.password}')
        
    def change_name(self, new_name):
        if len(new_name) in range(2, 10) and self.name != new_name:
            self.name = new_name
        elif self.name == new_name:
            print("Name already exists")
        else:
            print("Name must be between 2 and 10 characters")    
        
  
    def change_pin(self, new_pin):
        self.pin = new_pin
  
    def change_password(self, new_password):
        if new_password == self.password:
            print("Password already exists")
            return
        elif len(new_password) < 5:
            print("Password must be at least 5 characters")
            return
        self.password = new_password

class BankUser(User):
    def __init__(self, name, pin, password, balance = 0):
        super().__init__(name, pin, password)
        self.balance = balance
        
    def show_balance(self):
        print(f'{self.name} has an account balance of: ${self.balance:.2f}')
    
    def withdraw(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            print("\nInvalid deposit amount, please enter a number.\n")
            return
        
        if amount <= 0:
            print("Invalid withdrawal amount, please enter a positive amount.")
            return False
        if amount > self.balance:
            print("Insufficient funds")
            return False
        self.balance -= amount
        return True
    
    def deposit(self, amount):
        try:
            amount = int(amount)
        except ValueError:
            print("\nInvalid deposit amount, please enter a number.\n")
            return
        
        if amount <= 0:
            print("\nInvalid deposit amount, please enter a positive amount.\n")
            return
        self.balance += amount
    
    def transfer_money(self, other_user, amount):
        try:
            amount = int(amount)
        except ValueError:
            print("\nInvalid deposit amount, please enter a number.\n")
            return
        
        if amount <= 0:
            print("\nInvalid transfer amount, please enter a positive amount.\n")
            return False
        
        print(f"\nTransferring ${amount:.2f} from {self.name} to {other_user.name}")
        print("---Authentication Required ---")
        
        pin_input = int(input(f"Enter your PIN {self.name}: ") )
        if pin_input != self.pin:
            print("Invalid PIN. Transer failed.")
            return False
        
        if amount > self.balance:
            print("Insufficient funds")
            return False
        
        self.balance -= amount
        other_user.balance += amount
        print("\n--- Transfer Autherized ---")
        print(f"Transferred ${amount:.2f} from {self.name} to {other_user.name}")
        return True
    
    def request_money(self, other_user, amount):
        try:
            amount = int(amount)
        except ValueError:
            print("\nInvalid deposit amount, please enter a number.\n")
            return
        
        if amount <= 0:
            print("\nInvalid request amount, please enter a positive amount.\n")
            return False
        
        print("\n--- Requesting Money - Authentication Required ---")
        pin_input = int(input(f"Enter {other_user.name}'s PIN to request money: "))  # Prompt for the other user's PIN
        if pin_input != other_user.pin:
            print("Invalid PIN. Request failed.")
            return False
        
        password_input = input(f"Enter {self.name}'s password to confirm request: ")  # Prompt for the current user's password
        if password_input != self.password:
            print("Invalid password. Request failed.")
            return False
        
        if amount > other_user.balance:
            print(f"\n{other_user.name} has insufficient funds! Request failed.\n")
            return False
        
        other_user.balance -= amount
        self.balance += amount
        print(f"\nRequest sucessful. Transferred ${amount:.2f} from {other_user.name}")
        return True
            
  
  



""" Driver Code for Task 1 """
##test_user = User("John Doe", 1234, "password123")

""" Driver Code for Task 2 """
#test_user = User("John Doe", 1234, "password123")
#print(f'Name: {test_user.name}, Pin: {test_user.pin}, Password: {test_user.password}')
#test_user.change_name("Jane Doe")
#test_user.change_name("J")  # bad name
#test_user.change_name("John Doe")
#test_user.change_pin(5678)  # good pin
#test_user.change_pin(78)  # bad pin
#test_user.change_password("newpassword456")  # good password
#test_user.change_password("ne45")  # bad password

#print(f'Name: {test_user.name}, Pin: {test_user.pin}, Password: {test_user.password}')


""" Driver Code for Task 3"""

#test_user = BankUser("John Doe", 1234, "password123")
#print(f'Name: {test_user.name}, Pin: {test_user.pin}, Password: {test_user.password}, Balance: {test_user.balance}')

"""Driver Code for Task 4"""

#test_user = BankUser("John Doe", 1234, "password123")
#test_user.show_balance()
#test_user.deposit("dd")
#test_user.deposit(100)
#test_user.show_balance()
#test_user.withdraw(50)
#test_user.show_balance()


"""Driver Code"""
#user1 = BankUser("Alice", 1234, "alicepass", 500)
#user2 = BankUser("Bob", 5678, "bobpass", 300)

#user1.show_balance()
#user2.show_balance()

"""Testing Transfers"""
#user1.transfer_money(user2, 200)  # Alice sends $200 to Bob
#user1.transfer_money(user2, "ddd")  # Transfer with invalid amount
##user1.show_balance()
##user2.show_balance()

#"""Testing Requests"""
#user2.request_money(user1, 200) #Bob request 100 from Alice
#user1.show_balance()
#user2.show_balance()

