"""
02_data_types_and_conversion.py
--------------------------------
This program demonstrates:
- Basic Python data types: string, integer, float, boolean
- Type checking and type conversion (str ↔ int)
- Indexing strings
- Adding digits from user input
"""

# String examples
str1 = 'Hello'
str2 = "Python"

print(len(str1 + str2))    # Length of concatenated string "HelloPython"
print("Hello"[4])          # Indexing (prints 'o')
print(str1 + str2)         # Concatenation "HelloPython"

# Integer + Float
i = 123456
j = 123.456
print(i + j)               # Adding int + float

# Underscore for readability
i1 = 123_567_790
print(i1)

# Type conversion example
num_char = len(input("What is your name?\n"))
new = str(num_char)  # Convert int → str
print("Your name has " + new + " characters")

# Adding digits of a 2-digit number
two_digit = input("Enter a 2-digit number: ")
i = int(two_digit[0])
j = int(two_digit[1])
print(f"Sum of digits = {i + j}")
