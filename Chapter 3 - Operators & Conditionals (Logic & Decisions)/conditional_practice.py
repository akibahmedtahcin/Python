# 1. Grading System
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: Fail")

# 2. Time-based Greeting
hour = 14
if hour < 12:
    print("Good Morning")
elif hour < 18:
    print("Good Afternoon")
else:
    print("Good Night")

# 3. Traffic Light System
signal = "yellow"
if signal == "red":
    print("Stop!")
elif signal == "yellow":
    print("Get Ready!")
elif signal == "green":
    print("Go!")
else:
    print("Invalid signal")

# 4. Number Type Checker
num = 0
if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("The number is Zero")

# 5. Age Categorization
age = 25
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior Citizen")