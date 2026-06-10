n = int(input("Check your number is Prime or not: "))
count = 0

for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1  


if count == 2:
    print(f"{n} is a Prime Number (It has exactly 2 factors).")
else:
    print(f"{n} is not a Prime Number.")