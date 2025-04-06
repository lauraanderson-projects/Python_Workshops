import random

def guess_random_number(tries, start, stop):
    random_number = random.randint(start, stop)
    print(f"Random number is {random_number}")  # For debugging purposes
    while tries != 0:
        print(f"You have {tries} tries left")
        guess = int(input("Enter your guess: "))
        if guess == random_number:
            print("You guessed it!")
            break
        elif guess < random_number:
            print("Too low")
        else:
            print("Too high")
        tries -= 1
        
        if tries == 0:
            print("You lost!")
            
def guess_random_number_linear_search(tries, start, stop):
    random_number = random.randint(start, stop)
    #print(f"Random number is {random_number}")  # For debugging

    for guess in range(start, stop + 1):  # Linear search from start to stop
        if tries == 0:
            print("You lost!")
            return
        
        print(f"You have {tries} tries left")
        print(f"Computer guesses: {guess}")

        if guess == random_number:
            print("Computer guessed it!")
            return
        elif guess < random_number:
            print("Too low")
        else:
            print("Too high")
        
        tries -= 1

    print("Computer ran out of tries and lost!")
    
def guess_random_num_binary(tries, start, stop):
    random_number = random.randint(start, stop)
    print(f"Random number is {random_number}")  # For debugging
    
    lower_bound = start
    upper_bound = stop

    while tries != 0:
        guess = (lower_bound + upper_bound) // 2
        print(f"You have {tries} tries left")
        print(f"Computer guesses: {guess}")

        if guess == random_number:
            print("Computer guessed it!")
            break
        elif guess < random_number:
            print("Too low")
            lower_bound = guess + 1
        else:
            print("Too high")
            upper_bound = guess - 1

        tries -= 1

    if tries == 0:
        print("Computer ran out of tries and lost!")
    
 
# Example call
#guess_random_number(5, 1, 10)  # Example usage

# Example call
#guess_random_number_linear_search(5, 1, 10)

# Example call
guess_random_num_binary(5, 1, 10)  # Example usage