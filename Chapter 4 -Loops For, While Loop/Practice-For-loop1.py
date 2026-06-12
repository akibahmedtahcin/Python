# Loop through numbers from 1 to 20
for i in range(1, 21):
    # If the number is 10 or 15, skip it
    if i == 10 or i == 15:
        continue
    
    # Print the remaining numbers
    print(i)