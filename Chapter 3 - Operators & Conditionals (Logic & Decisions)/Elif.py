# 1. Weather Advisory 
temperature = 30
if temperature > 35:
    print("It's a hot day!")
elif temperature > 25:
    print("It's a pleasant day.")
else:
    print("It's a cold day.")

# 2. Parking Fee System 
hours = 3
if hours <= 1:
    print("Fee: $2")
elif hours <= 3:
    print("Fee: $5")
else:
    print("Fee: $10")

# 3. ATM Withdrawal 
balance = 1000
withdraw = 1200
if withdraw > balance:
    print("Insufficient Balance!")
elif withdraw > 500:
    print("Large withdrawal detected.")
else:
    print("Transaction Successful.")

# 4. Password Strength 
length = 5
if length >= 8:
    print("Strong Password")
elif length >= 5:
    print("Medium Password")
else:
    print("Weak Password")