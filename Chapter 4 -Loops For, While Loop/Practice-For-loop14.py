text = input("Enter a string: ")


reversed_text = ""
for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]


if text == reversed_text:
    print(f"'{text}' is a Palindrome.")
else:
    print(f"'{text}' is not a Palindrome.")