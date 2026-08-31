a = 10
b = 20
c = 6

# ℹ️ Addition

print(f"a + b = {a + b}")

# ℹ️ Subtraction
print(f"a - b = {a - b}")
# ℹ️ Division
print(f"a / b = {a / b}")
# ℹ️ Multiplication
print(f"a * b = {a * b}")
# ℹ️ Modulus
print(f"b % c = {b % c}")

"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Ask user for Monthly Income (float).
[ ] 3. Ask user for 5 DIFFERENT expense amounts (float).
[ ] 4. Calculate Total Expenses and Remaining Balance.
[ ] 5. Calculate Percentage of Income Spent.
[ ] 6. Output formatted to 2 decimal places (:,.2f or :.2%).
-----------------------------------------------------------------------
"""

gross_income = float(input("What is your gross monthly income? "))
rent_mortgage = float(input("How much do you spend on either rent or mortgage each month? "))
car = float(input("How much do you spend monthly on your car? "))
phone = float(input("How much do you spend on your phone each month? "))
food = float(input("How much do you spend, roughly, on food each month? "))
entertainment_activities = float(input("How much do you spend, roughly, on entertainment/ activities each month? "))
wifi = float(input("What do you spend, monthly, on your wifi? "))
basic_necessities = float(input("What do you spend, roughly, on basic necessities each month? "))

net_income = gross_income * .8
total_expenses = rent_mortgage + car + phone + food + entertainment_activities + wifi + basic_necessities
remaining = net_income - total_expenses

print(f"You've spent a total of {total_expenses: ,.2f}")
print (f"That was {total_expenses/net_income: .2%}")