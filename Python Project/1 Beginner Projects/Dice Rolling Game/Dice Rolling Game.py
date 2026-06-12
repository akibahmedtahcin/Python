# #Dice Rolling Game.py
# # Ask: roll the dice?
# # If user enters y
# #Generate two random numbe
# Print them
# # If user enters n
# Print thank you message
# Terminate
# # Else
# Print invalid choice
#Loop
import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()

    if choice == 'y':
        # Generating two random numbers between 1 and 6
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        
        print(f'You rolled: ({die1}, {die2})')
        
    elif choice == 'n':
        print('Thanks for playing!')
        break
        
    else:
        print('Invalid choice. Please enter "y" or "n".')