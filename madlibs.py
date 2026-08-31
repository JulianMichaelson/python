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
# 📝 Collect 9 different words from the player to build the story

name = input("Please enter a person's name: ")
color_toy = input("Please enter a toy color: ")
toy = input("Please enter a toy: ")
item = input("Please enter a type of item: ")
color = input("Please enter a color: ")
color_fur = input("Please enter fur color: ")
color_spots = input("Please enter spots color: ")
wrapping_color = input("Please enter a wrapping color: ")
character = input("Please enter a character: ")
food = input("please enter a food: ")

# ℹ️ Output
print("Mad Lib for The Wonderful Christmas Morning\n\n")  # \n creates blank lines for formatting
print(f"{name} woke up Christmas Morning, ecstatic to see the land of snow outside")  # 🎭 Story begins with name
print(f"{name} ran quickly downstairs to the living room and looked under the beautifully decorated, gleaming, Christmas Tree")  # 🎭 Continues story
print(f"{name} was greeted by 4 presents, some long, short, wide, thin")  # 🎭 Sets up gifts
print(f"The first present was a brand new, all {color_toy} {toy}. That toy came with a {item}")  # 🎁 Uses color_toy + toy + item
print(f"After opening the first present, {name} opened a second one. It was a bigger gift, {color} in color.")  # 🎁 Uses color
print(f" After unwrapping it and removing the top, {name} was overjoyed to see that it was a puppy! With {color_fur} fur and {color_spots} spots")  # 🐕 Uses color_fur + color_spots
print(f"{name} then opened their 3rd present, a big present wrapped in {wrapping_color}. Once unwrapped it was seen to be a {character} action figure")  # 🎁 Uses wrapping_color + character
print(f"Their final present was the largest amongst all. Shiny in color, littered with polka dots. Once opened , out came his Mother, to give him a Christmas Hug. After their endearing moment they went and ate {food}")  # 🎉 Story finale with food
