# Range Basics: Print numbers from 1 to 5
a=range(1,20, 6)

for i in a:
    print(i)

# String Iteration (Character access): Directly access characters in a string

word = "Python"
for char in word:
    print(char)

# String Iteration (Index access): Use range() and len() to get index values.

word = "Python"
for i in range(len(word)):
    print(f"Index {i} is {word[i]}")

# Step Iteration: Print only even numbers up to 10.
for i in range(2, 11, 2):
    print(i)

# Reverse Iteration: Count down using a negative step.
for i in range(5, 0, -1):
    print(i)

# List Iteration: Loop through a collection of items.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Calculating Squares: Compute the square of numbers 1-5.
for i in range(1, 6):
    print(f"Square of {i} is {i*i}")

# Multiplication Table: Generate a table for a number.
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")