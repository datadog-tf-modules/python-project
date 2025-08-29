"""
01_strings_and_inputs.py
-------------------------
This program demonstrates:
- Taking input from user (city & pet name)
- Printing outputs using:
    1. f-strings with tab space
    2. String concatenation with +
    3. Clean f-string formatting
"""

# Example 1: f-string with tab
print("welcome to python")
city = input("what is your city: ")
name = input("whats your pet name: ")
print(f'you are from {city}\tand your pet name is {name}')

# Example 2: concatenation
print("welcome to the band name generator")
city = input("which city did you grow up in?\n")
pet = input("what is your pet name?\n")
print("your band name could be " + city + " " + pet)

# Example 3: f-string (cleaner)
print("welcome to the band name generator")
city = input("which city did you grow up in?\n")
pet = input("what is your pet name?\n")
print(f"your band name could be {city} {pet}")
