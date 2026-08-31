"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS (DO NOT DELETE)
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a String variable.
[ ] 3. Define an Integer variable.
[ ] 4. Define a Float variable.
[ ] 5. Define a Boolean variable.
[ ] 6. Print all variables using F-Strings.
[ ] 7. Upload to GitHub.
-----------------------------------------------------------------------
"""

print("double quotes")
print('single quotes')

print('print "double quotes"')
print("Print 'single quotes'")
print("Or use escape \" or ' to print quotes")
integer = 1
my_int = "1"

# These values look similar, but integer is a number and my_int is text.
# print("Adding number to a string:")
# print(integer + my_int)

print("Adding strings: ")
print(my_int + my_int)
# Joining two strings puts their text together, so the result is "11".

print("Adding numbers:")
print(integer + integer)
# Adding two integers performs arithmetic, so the result is 2.


# Booleans represent a True or False value.
tired = True
awake = True
coffee = False

print(coffee)
# This block runs because tired is True.
if tired:
        print("I need coffee")

--------------------------------------------------------------------------------------------------------------------------
# RPG Character Profile Assignment Portion
character_name = "Julian"
height = "6'0"
weight = 160
skin_color = "Tan"

print(f"Name: {character_name}")
print(f"Height: {height}")
print(f"Weight: {weight}")
print(f"Skin Tone: {skin_color}")

item_name = "Orbs of Healing"
quantity = 5
price = 30.25
orbs_on_sale = True

print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"{item_name} cost {character_name} {price} for 1, {character_name} has {quantity}. Costing him a total of $151.25")
print(f"On Sale: {orbs_on_sale}")

weapon_type_and_name = "Sword of Falabath"
damage = 45
sword_price = 1000
sword_on_sale = False

print(f"Weapon: {weapon_type_and_name}")
print(f"Damage: {damage}")
print(f"Price: {sword_price}")
print(f"On Sale: {sword_on_sale}")

armor_name = "Armor of Falabath"
protection = 85
armor_price = 1500
armor_on_sale = False

print(f"Armor: {armor_name}")
print(f"Protection: {protection}")
print(f"Price: {armor_price}")
print(f"On Sale: {armor_on_sale}")
