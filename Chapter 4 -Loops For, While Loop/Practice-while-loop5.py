# Number of terms to display
n = 10

# Initialize the first two numbers
a = 0
b = 1
count = 0

print("Fibonacci series:")

# Using while loop to generate the series
while count < n:
    print(a, end=" ")
    
    # Calculate the next term
    nth = a + b
    
    # Update values for the next iteration
    a = b
    b = nth
    
    # Increment the counter
    count += 1