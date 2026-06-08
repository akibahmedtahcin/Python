# # Q1. Greatest between two numbers
# num1 =10
# num2 = 20
# if num1 > num2:
#     print(f"{num1} is greater than {num2}")\

# # Q2. Greeting based on gender
# gender = input("Enter your gender(M/F): ").upper()
# if gender == "M":
#      print("Hello, Sir!")
# elif gender == "F":
#      print("Hello, Ma'am!")
# else:
#      print("Invalid input.")

# # Q3. Check Even or Odd
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is even.")
# else:
#     print(f"{num} is odd.")
# # Q4. Valid Voter Checker
# age = int(input("Enter your age: "))
# has_id = input("Do you have a valid ID? (yes/no): ").lower()    

# if age >= 18:
#     if has_id == "yes":
#         print("You are eligible to vote.")
#     else:
#         print("You need a valid ID to vote.")
# else:
#     print("You are not old enough to vote.")
# # Q5. Leap Year Checker
# year = int(input("Enter a year: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year.") # Leap Year
#         else:
#             print(f"{year} is not a leap year.") # Not a Leap Year
#     else:
#         print(f"{year} is a leap year.") # Leap Year
# else:
#     print(f"{year} is not a leap year.") # Not a Leap Year