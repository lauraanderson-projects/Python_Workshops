def show_balance(balance):
	print(f"\nYour current balance is: ${balance:.2f}\n")

def deposit(balance):
	try:
		amount = float(input("Enter deposit amount: "))
		if amount <= 0:
			print("Invalid amount. Please enter a positive number.")
			return balance
		balance += amount
		print(f"Deposit successful! Your new balance is: ${balance:.2f}")
	except ValueError:
		print("Invalid input. Please enter a valid number.")
	return balance

def withdraw(balance):
	try:
		amount = float(input("Enter withdrawal amount: "))
		if amount <= 0:
			print("Invalid amount. Please enter a positive number.")
			return balance
		if amount > balance:
			print("Insufficient funds for this withdrawal.")
			return balance
		balance -= amount
		print(f"Withdrawal successful! Your new balance is: ${balance:.2f}")
	except ValueError:
		print("Invalid input. Please enter a valid number.")
	return balance

def logout():
	print("\nThank you for using our ATM. Goodbye!\n")
	return False