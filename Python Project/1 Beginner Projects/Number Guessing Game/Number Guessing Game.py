#  Generate a random number
#  Ask the user to make a guess
#  If not a valid number
# Print an error
# If number < guess
# Print too low
#  If number > guess
# Print too high
# Else
# Print well done
import random

# Generate the random number once outside the loop
number_to_guess = random.randint(1, 100)

print("I have generated a random number between 1 and 100.")

while True:
    try:
        # Ask the user to make a guess
        guess = int(input("Enter your guess: "))
        
        # Check the guess
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Well done! Congratulations! You guessed the correct number.")
            break  # Exit the loop when the guess is correct
            
    except ValueError:
        # Print an error if input is not a valid integer
        print("Invalid input! Please enter a valid number.")