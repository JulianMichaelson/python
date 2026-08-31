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

# 💬 STRINGS - Text data in Python
print("double quotes")  # 🔤 Single and double quotes both work
print('single quotes')  # 💡 Pick one style and stay consistent

# 🛡️ ESCAPING - Special characters inside strings
print('print "double quotes"')  # 📝 Single quotes allow double quotes inside
print("Print 'single quotes'")  # 📝 Double quotes allow single quotes inside
print("Or use escape \" or ' to print quotes")  # ↖️ Backslash escapes special characters
# 🔢 DATA TYPES - Different kinds of data
integer = 1  # 📊 Integer: whole number
my_int = "1"  # 📝 String: text (notice the quotes!)

# 💡 TIP: 1 and "1" are DIFFERENT! Numbers can do math, strings cannot.
# print("Adding number to a string:")
# print(integer + my_int)  # ❌ This would cause an error!

# 🔗 STRING CONCATENATION - Joining strings together
print("Adding strings: ")
print(my_int + my_int)  # ➕ Combines "1" + "1" = "11" (text, not math!)
# 💡 TIP: With strings, + means join, NOT add!

# 🧮 ARITHMETIC - Math with numbers
print("Adding numbers:")
print(integer + integer)  # ➕ Adds 1 + 1 = 2 (actual math!)
# 💡 TIP: With numbers, + performs addition


# ✅ BOOLEANS - True or False values (used for decisions)
tired = True  # ✔️ True
awake = True  # ✔️ True
coffee = False  # ❌ False

print(coffee)  # Prints: False
# 🔀 CONDITIONALS - Do something IF a condition is true
if tired:  # Check if tired is True
        print("I need coffee")  # ✔️ This runs because tired is True


# ⚔️ RPG CHARACTER PROFILE - Multiple data types working together
character_name = "Julian"  # 📝 String
height = "6'0"  # 📝 String (height includes units)
weight = 160  # 📊 Integer (pounds)
skin_color = "Tan"  # 📝 String

# 🎯 F-STRINGS - Insert variables into text
print(f"Name: {character_name}")  # 🔤 Variables go inside curly braces
print(f"Height: {height}")
print(f"Weight: {weight}")
print(f"Skin Tone: {skin_color}")

# 🛍️ INVENTORY ITEM
item_name = "Orbs of Healing"  # 📝 String
quantity = 5  # 📊 Integer
price = 30.25  # 💰 Float (decimal number)
orbs_on_sale = True  # ✅ Boolean

print(f"Item: {item_name}")
print(f"Quantity: {quantity}")
print(f"{item_name} cost {character_name} ${price} for 1, {character_name} has {quantity}. Costing him a total of $151.25")  # 💡 Multiple variables in one f-string
print(f"On Sale: {orbs_on_sale}")

# ⚔️ WEAPON STATS
weapon_type_and_name = "Sword of Falabath"  # 📝 String
damage = 45  # 📊 Integer (damage points)
sword_price = 1000  # 💰 Integer (gold)
sword_on_sale = False  # ❌ Boolean

print(f"Weapon: {weapon_type_and_name}")
print(f"Damage: {damage}")
print(f"Price: {sword_price}")
print(f"On Sale: {sword_on_sale}")

# 🛡️ ARMOR STATS
armor_name = "Armor of Falabath"  # 📝 String
protection = 85  # 📊 Integer (defense points)
armor_price = 1500  # 💰 Integer (gold)
armor_on_sale = False  # ❌ Boolean

print(f"Armor: {armor_name}")
print(f"Protection: {protection}")
print(f"Price: {armor_price}")
print(f"On Sale: {armor_on_sale}")

# 💡 KEY TAKEAWAYS:
# 📝 Strings hold text
# 📊 Integers hold whole numbers
# 💰 Floats hold decimals
# ✅ Booleans hold True/False
# 🎯 F-strings let you insert variables into text# Booleans represent a True or False value.
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
