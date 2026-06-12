# Taking an integer input from the user
num = int(input("Enter a number (e.g., 1234): "))

# Creating a copy of the number to preserve the original value
temp = num 
total_sum = 0

# Loop runs until temp becomes 0
while temp > 0:
    # Use modulo (%) to get the last digit
    digit = temp % 10    
    
    # Add the extracted digit to total_sum
    total_sum += digit   
    
    # Use floor division (//) to remove the last digit
    temp = temp // 10    

# Display the final result
print(f"The sum of the digits of {num} is: {total_sum}")