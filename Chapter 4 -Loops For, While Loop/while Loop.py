# 1. WHILE LOOP EXAMPLES
print("--- While Loop Examples ---")

# Countdown
timer = 5
while timer > 0:
    print(f"Countdown: {timer}")
    timer -= 1

# Summing until 50
total = 0
num = 1
while total < 50:
    total += num
    num += 1
print(f"Total reached: {total}")

# 2. FOR LOOP EXAMPLES
print("\n--- For Loop Examples ---")

# Simple Range
for i in range(1, 6):
    print(f"Number: {i}")

# Iterating over string
word = "Python"
for char in word:
    print(f"Character: {char}")

# Multiplication Table of 5
n = 5
for i in range(1, 11):
    print(f"{n} x {i} = {n*i}")

# Square calculation
for i in range(1, 6):
    print(f"Square of {i} is {i*i}")