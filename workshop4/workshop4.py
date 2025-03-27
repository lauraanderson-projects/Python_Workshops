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