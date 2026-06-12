# Taking an integer input from the user
n = int(input("Enter a number (n): "))

# Starting point
i = 1

# Loop runs from 1 up to n
while i <= n:
    # Check if the current number 'i' is divisible by 3
    if i % 3 == 0:
        print(i)
    
    # Increment 'i' to move to the next number
    i = i + 1