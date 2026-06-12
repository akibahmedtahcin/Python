while True:
    # Displaying the menu options to the user
    print("\n--- MENU ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Quit")
    
    # Taking user choice as input
    choice = input("Enter your choice (1/2/3): ")
    
    # Checking if the user wants to quit
    if choice == '3':
        print("Exiting the program. Goodbye!")
        break  # This command stops the loop
        
    # Checking for valid operations
    elif choice in ('1', '2'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if choice == '1':
            print(f"Result: {num1 + num2}")
        else:
            print(f"Result: {num1 - num2}")
            
    # Handling invalid inputs
    else:
        print("Invalid choice! Please select 1, 2, or 3.")