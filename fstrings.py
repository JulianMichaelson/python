# ""
# fstring formatting in Python-
# this makes it easier to use variables, format numbers, left align, right align, etc. There is a Python F-String cheat sheet in module 0
# ""

# # fstrings for variables

# name = "Julian"
# age = 20

# print (f"{name} is age and will be {age + 1} next year.")  # 📍 variables 📊 expressions

# # Alignment
# # the number after the colon and symbol is your column width

# print (f"{name:<30}")  # ⬅️ left align, 30 char wide
# print (f"{name:>30}")  # ➡️ right align, 30 char wide
# print (f"{name:^30}")  # 🎯 center align, 30 char wide

# # Line below is creating two columns 30 wide centering name and age
# print(f"({name:^30} {age:^30}")  # 🎯🎯 two centered columns

score_1 = 1088
score_2 = 1073
score_3 = 1065

average = (score_1 + score_2 + score_3) / 3

print(average)
print(f"{average: ,.0f}")  # 💰 comma separator, 🔢 zero decimals

distance_to_monroe = 852
distance_to_phoenix = 1712

print(f"Distance to Monroe, North Carolina {distance_to_monroe: ,.0f}")  # 💰 formatted number
print(f"Distance to Phoenix, Arizona {distance_to_phoenix: ,.0f}")  # 💰 formatted number

current_mort_rate = .0675
print(f"Mortgage rate = {current_mort_rate:.2%}")  # % converts to percentage, 🔢 2 decimals