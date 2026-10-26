"""
-----------------------------------------------------------------------
ASSIGNMENT 10A: THE RESILIENT PIZZA ENGINE
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constant TOPPINGS defined as a Tuple in ALL_CAPS.
[ ] 3. Function 'make_pizza' defines 4 specific parameters.
[ ] 4. 'make_pizza' uses a DEFAULT value for is_delivery.
[ ] 5. main() displays the Global Pantry list to the user.
[ ] 6. main() calls the function using KEYWORD ARGUMENTS.
-----------------------------------------------------------------------
"""
SIZE = ("Extra Large (18 Inches)", "Large (15 Inches)", "Medium (12 Inches)", "Small (10 Inches)")
TOPPINGS = ("Pepperoni", "Sausage", "Banana Peppers", "Ham", "Onions", "Mushrooms", "Bacon", "Pineapple")
CRUST = ("Thin", "Cheese Stuffed", "Pepperoni Stuffed", "Thick", "Chicago-Style", "New York-Style")

def make_pizza(size, crust, topping, is_delivery=True):
    is_delivery = "Delivery" if is_delivery else "Pickup"

    print("\n---YOUR PIZZA ORDER---")
    print(f"Size: {size}")
    print(f"Topping: {topping}")
    print(f"Crust: {crust}")
    print(f"Order type: {is_delivery}")

def main():
    print(f"Pizza Sizes: {SIZE}")
    print(f"Available toppings: {TOPPINGS}")
    print(f"Available crust types: {CRUST}")

    size = input("Pizza size: ").title()
    topping = input("Choose a topping: ").title()
    crust = input("Crust type: ").title()

    make_pizza(
        size=size,
        crust=crust,
        topping=topping,
    )

main()

