# Chapter 03: Assignment Operators Practice
# এই ফাইলটি Compound Assignment Operators বোঝার জন্য

# ১. Addition and Assignment
x = 10
x += 5  # x = x + 5
print(f"After += : {x}") 

# ২. Subtraction and Assignment
y = 20
y -= 5  # y = y - 5
print(f"After -= : {y}")

# ৩. Multiplication and Assignment
z = 5
z *= 3  # z = z * 3
print(f"After *= : {z}")

# ৪. Division and Assignment
a = 20
a /= 4  # a = a / 4
print(f"After /= : {a}")

# ৫. Modulus and Assignment
b = 10
b %= 3  # b = b % 3
print(f"After %= : {b}")

# ৬. Exponentiation and Assignment
c = 2
c **= 3 # c = c ** 3
print(f"After **= : {c}")

# ছোট চ্যালেঞ্জ:
# একটি ভেরিয়েবল score = 10 নিন
# প্রথমে এতে 20 যোগ করুন (+=), তারপর একে 2 দিয়ে গুণ করুন (*=)
score = 10
score += 20
score *= 2
print(f"Final Challenge Score: {score}")