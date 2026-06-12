n = int(input("Tell me the number: "))

even_sum = 0
odd_sum = 0  # 1. Initialize odd_sum to 0

for i in range(1, n + 1):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i  # 2. Add the value of i, not 1

# 3. Move the print outside the loop so it prints only once
print(f"The sum of even numbers is {even_sum} and the sum of odd numbers is {odd_sum}")