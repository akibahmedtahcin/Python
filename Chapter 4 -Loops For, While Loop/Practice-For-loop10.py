n = int(input("Tell me the number whose factors you want: "))

print(f"The factors of {n} are:")

for i in range(1, n + 1):
    if n % i == 0:
        print(i)