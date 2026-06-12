# 1. Valid Voting Age
age = 14
has_id = True
if age >= 18 and has_id:
    print("You can vote")
else:
    print("Cannot vote")

# 2. Grade System
marks = 50
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")

# 3. Number Checker
num = -5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 4. Weekend Checker
day = "Friday"
if day == "Friday" or day == "Saturday":
    print("It's a weekend!")
else:
    print("It's a workday.")

# 5. Eligibility Criteria
age = 25
if 20 <= age <= 30:
    print("Eligible for the project")
else:
    print("Not eligible")

# 6. Password Validator
password = input("Enter password: ")
if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

# 7. Max of Three Numbers
n1, n2, n3 = 10, 25, 15
if n1 >= n2 and n1 >= n3:
    print(f"Largest: {n1}")
elif n2 >= n1 and n2 >= n3:
    print(f"Largest: {n2}")
else:
    print(f"Largest: {n3}")

# 8. Nested Decision (Check > 10 and Even/Odd)
x = 12
if x > 10:
    if x % 2 == 0:
        print("Greater than 10 and Even")
    else:
        print("Greater than 10 and Odd")
else:
    print("10 or less")