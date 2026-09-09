"""
-----------------------------------------------------------------------
ASSIGNMENT: 3B - The Buffet Calculator (Daily Specials)
DATE: [Insert Date]
FILE: buffet.py
-----------------------------------------------------------------------
REQUIREMENTS:
1. Ask the user for their age (convert to int) and the day of the week (convert to string).
2. Calculate the base price using if/elif/else:
   - Under 1: FREE ($0.00)
   - 1 to 11: $1.00 per year of age (Example: 5 years = $5.00)
   - 12 to 64: $16.95 (Standard Adult)
   - 65 and older: $12.95 (Senior Discount)
3. Use a match/case statement to handle special daily rules based on the day entered:
   - Tuesday: Children through age 12 are half price!
   - Sunday: Drinks are free!
   - Other days: Standard buffet pricing in effect.
4. Print the final price formatted as currency and display any applicable daily special notices.
-----------------------------------------------------------------------
"""

current_day_of_the_week = input("What day of the week is it?: ").lower()
match current_day_of_the_week.lower():
    case "sunday":
        child_price_per_year = 1.000
        print("Drinks are free!")
    case "tuesday":
        child_price_per_year = 0.50
        print("Children that are through age 12 are half price!")
    case _:
        child_price_per_year = 1.000
        print("Standard buffet pricing in effect.")



age = int(input("How old are you? "))
if age < 1:
    price = 0 #Free
    print("You eat for free")
    
elif age <= 11:
    price = age * child_price_per_year

elif age <= 64:
    price = 16.95

elif age >= 65:
    price = 12.95
    print("Senior Discount!!")

print(f"Your total amounts to ${ price: .2f}. Have a great time and enjoy your food!")



