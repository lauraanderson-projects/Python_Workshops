class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password
        
        print(f'Name: {self.name}, Pin: {self.pin}, Password: {self.password}')
        
    def change_name(self, new_name):
        self.name = new_name
  
    def change_pin(self, new_pin):
        self.pin = new_pin
  
    def change_password(self, new_password):
        self.password = new_password
  
  



""" Driver Code for Task 1 """
#test_user = User("John Doe", 1234, "password123")

""" Driver Code for Task 2 """
test_user = User("John Doe", 1234, "password123")
test_user.change_name("Jane Doe")
test_user.change_pin(5678)
test_user.change_password("newpassword456")

print(f'Name: {test_user.name}, Pin: {test_user.pin}, Password: {test_user.password}')