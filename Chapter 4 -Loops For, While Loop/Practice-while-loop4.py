# Set the secret number
secret_number = 7

# Initialize the guess variable with a value that is not 7
guess = 0

print("--- Welcome to the Lottery Guessing Game! ---")
print("I have chosen a number between 1 and 10. Can you guess it?")

# The loop continues until the user guesses the correct number
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    
    # Check if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed it right.")
    
    # Provide hints if the guess is incorrect
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")