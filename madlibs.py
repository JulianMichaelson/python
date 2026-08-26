"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included (Copy and paste THIS comment from opening to closing quotes).
[ ] 2. Program asks for at least 5 different inputs (variables).
[ ] 3. Output uses F-Strings to combine text and variables.
[ ] 4. Output uses at least one escape sequence (\n or \t).
[ ] 5. Code contains comments explaining the steps.
[ ] 6. Program runs without errors.
-----------------------------------------------------------------------
"""

# ℹ️Information Only
# 🆘HELP!


# ℹ️Declare Variables
name = "" # ℹ️ initializes the variable (optional)
animal = ""
color = ""


# ℹ️ Get User Input

name = input("Please enter a person's name: ")
item = input("Please enter a type of item: ")
color = input("Please enter a color: ")
color_toy = input("Please enter a toy color: ")
color_fur = input("Please enter fur color: ")
color_spots = input("Please enter spots color: ")
toy = input("Please enter a toy: ")

# ℹ️ Output
print("Mad Lib for The Wonderful Christmas Morning\n\n")
print(f"{name} woke up Christmas Morning, ecstatic to see the land of snow outside")
print(f"{name} ran quickly downstairs to the living room and looked under the beautifully decorated, gleaming, Christmas Tree")
print(f"{name} was greeted by 4 presents, some long, short, wide, thin")
print(f"The first present was a brand new, all {color_toy} {toy}")
print(f"After opening the first present, {name} opened a second one. It was a bigger gift, {color} in color.")
print(f" After unwrapping it and removing the top, {name} was overjoyed to see that it was a puppy! With {color_fur} fur and {color_spots} spots")
print(f"")