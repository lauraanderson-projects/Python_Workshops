def login(database, username, password):
    #database = {"admin": "password123",}  # Example user database
    # Check if the username exists in the database and if the password matches
    # Note: The database should be passed as an argument to avoid hardcoding
    
    username = username.strip()  # Remove any leading/trailing whitespace
    password = password.strip()  # Remove any leading/trailing whitespace
    
    if username in ["admin", "Admin", "ADMIN"]:
        username = "admin"  # Normalize admin username to lowercase for consistency
    
    # Check if the username and password match the stored values in the database
    if username in database and database[username] == password:
        print(f"\nWelcome back, {username}!")
        return username  # Return the username upon successful login
    elif username in database and database[username] != password:
        print("\nIncorrect password.")
        return ""
    elif username not in database:
        print("\nUsername not found. Please register first.")
        return ""
    else:
        print("\nInvalid username or password.")
        return ""  # Return an empty string if login fails

def register(database, username, password):
    #database = {"admin": "password123",}  # Example user database
    # Check if the username already exists in the database
    
    username = username.strip()  # Remove any leading/trailing whitespace
    password = password.strip()  # Remove any leading/trailing whitespace
    
    # Normalize the "admin" username to lowercase for consistency
    if username in ["admin", "Admin", "ADMIN"]:
        username = "admin"  # Normalize admin username to lowercase for consistency
        
    # Check if the username already exists in the database
    if username in database:
        print("\nUsername already registered.")
        return ""  # Return an empty string if username already exists
    
    # Check if the password is at least 5 characters long
    if len(username) > 10:
        print("\nUsername must be not exceed 10 characters.")
        return "" # Return an empty string if username is too long.
    if len(password) < 5:
        print("\nPassword must be at least 5 characters long.")
        return ""
    
    # Register the new user by adding them to the database
    database[username] = password  # Add the new user to the database
    print(f"\nUser {username} registered successfully.")
    return username  # Return the username upon successful registration