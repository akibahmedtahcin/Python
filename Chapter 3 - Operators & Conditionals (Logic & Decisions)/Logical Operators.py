# --- Part 1: Initial Logic ---
a = 10
b = 5
print(f"Result 1: {a > 5 and b < 10}")  # True
print(f"Result 2: {a > 20 or b < 10}")  # True
print(f"Result 3: {not (a > 5)}")       # False

# --- Part 2: Basic Comparison ---
print(f"Result 4: {5 > 3 and 2 < 4}")   # True
print(f"Result 5: {5 > 3 or 2 > 4}")    # True
print(f"Result 6: {not (5 > 3)}")       # False
print(f"Result 7: {not (2 > 4)}")       # True

# --- Part 3: image_058ae1.png Exercises ---
print(f"Exercise 1: {126 > 130}")       # False
print(f"Exercise 2: {(456 == 456) != (235 == 236)}") # True
print(f"Exercise 3: {12 < 10 or 45 == 56 or 69 > 70 or 15 != 13}") # True
print(f"Exercise 4: {True and bool(0)}") # False
print(f"Exercise 5: {True and bool(6)}") # True