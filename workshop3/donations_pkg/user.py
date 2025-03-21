def login(database, username, password):
    #database = {"admin": "password123",}  # Example user database
    # Check if the username exists in the database and if the password matches
    # Note: The database should be passed as an argument to avoid hardcoding
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

def register(database, username):
    #database = {"admin": "password123",}  # Example user database
    # Check if the username already exists in the database
    if username in database:
        print("\nUsername already registered.")
        return ""  # Return an empty string if username already exists
    else:
        print(f"\nUser {username} registered successfully.")
        return username  # Return the username upon successful registration