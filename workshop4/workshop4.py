class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
        
        #print(f'Name: {self.name}, Pin: {self.pin}, Password: {self.password}')
        
    def change_name(self, new_name):
        self.name = new_name
  
    def change_pin(self, new_pin):
        self.pin = new_pin
  
    def change_password(self, new_password):
        self.password = new_password

class BankUser(User):
    def __init__(self, name, pin, password, balance = 0):
        super().__init__(name, pin, password)
        self.balance = balance
        
    def show_balance(self):
        print(f'Balance for {self.name}: {self.balance}')
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return False
        self.balance -= amount
        return True
    
    def deposit(self, amount):
        self.balance += amount
    
    def transfer_money(self, other_user, amount):
        pin_input = int(input(f"Enter your PIN {self.name}: ") )
        
        if pin_input != self.pin:
            print("Invalid PIN. Transer failed.")
            return False
        
        if amount > self.balance:
            print("Insufficient funds")
            return False
        
        self.balance -= amount
        other_user.balance += amount
        print(f"\nTransferred ${amount} from {self.name} to {other_user.name}")
        return True
    
    def request_money(self, other_user, amount):
        pin_input = int(input(f"Enter {other_user.name}'s PIN to request money: "))  # Prompt for the other user's PIN
        if pin_input != other_user.pin:
            print("Invalid PIN. Request failed.")
            return False
        
        password_input = input(f"Enter {self.name}'s password to confirm request: ")  # Prompt for the current user's password
        if password_input != self.password:
            print("Invalid password. Request failed.")
            return False
        
        if amount > other_user.balance:
            print(f"{other_user.name} has insufficient funds! Request failed.")
            return False
        
        other_user.balance -= amount
        self.balance += amount
        print(f"\nRequest sucessful. Transferred ${amount} from {other_user.name}")
        return True
            
  
  



""" Driver Code for Task 1 """
#test_user = User("John Doe", 1234, "password123")

""" Driver Code for Task 2 """
"""
test_user = User("John Doe", 1234, "password123")
test_user.change_name("Jane Doe")
test_user.change_pin(5678)
test_user.change_password("newpassword456")

print(f'Name: {test_user.name}, Pin: {test_user.pin}, Password: {test_user.password}')
"""

""" Driver Code for Task 3"""
"""
test_user = BankUser("John Doe", 1234, "password123")
print(f'Name: {test_user.name}, Pin: {test_user.pin}, Password: {test_user.password}, Balance: {test_user.balance}')
"""

""" Driver Code for Task 4"""
"""
test_user = BankUser("John Doe", 1234, "password123")
test_user.show_balance()
test_user.deposit(1000)
test_user.show_balance()
test_user.withdraw(100)
test_user.show_balance()
"""

# Driver Code
user1 = BankUser("Alice", 1234, "alicepass", 500)
user2 = BankUser("Bob", 5678, "bobpass", 300)

# Testing Transfers
"""
user1.show_balance()
user2.show_balance()

user1.transfer_money(user2, 200) #Alice send 200 to Bob
user1.show_balance()
user2.show_balance()
"""

# Testing Mondy Request

user2.request_money(user1, 100) #Bob request 100 from Alice
user1.show_balance()
user2.show_balance()