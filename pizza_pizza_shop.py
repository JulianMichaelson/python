# GLOBAL CONSTANTS (Sizes, Pizza Choices, Pizza Type, Drinks, Sides, Price)
SIZES = ("Small", "Medium", "Large", "Extra Large")
PIZZA_CHOICES = ("Pepperoni", "Cheese", "Sausage", "Meat Lovers", "Veggie")
PIZZA_TYPE = ("Thin Crust", "Thick Crust", "Chicago Style", "New York Style", "Detroit Style", "Stuffed Crust")
DRINKS = ("Water", "Coke", "Dr. Pepper", "Lemonade", "Sweet Tea", "Beer")
SIDES = ("5 Count Buffalo Wings", "5 Count BBQ Wings", "5 Count Hot Wings", "5 Count Garlic Parmesan Wings", "5 Count Lemon Pepper Wings", "Salt and Vinegar Chips", "Sour Cream and Onion Chips", "5 Count Mozzarella Sticks with Marinara")
MENU = "menu.txt"

def login():
    # Gets the users information like their name
    # will see if the user is already existing
    pass

def past_orders():
    # It will check and show if there are any past orders, it will show so if there are any
    # Have the option to past order(s)
    pass

def menu():
    # Will show a list of the pizza choices alongside sides, types, drinks, etc
    pass

def pizza_order():
    # displays all food choices, types, sides and drinks and will ask you to pick in selection
    pass

def order_review():
    # shows you all your selected choices to confirm back to you if all is correct
    # can change or confirm the order
    # total price for the whole order
    pass

def save_order(order):
    # Order is saved to the file
    pass

def order_receipt(order):
    # Display final order
    pass

# Main traditionally is coded at the end of the page so the other functions are loaded first
def main():
    # main organizes all of the functions
    id = login()
    saved = past_orders(id)
    # if saved order chosen move skip new order
    order = pizza_order(id)
    approved = order_review(order)
    # if approved save - otherwise change
    save_order(order)
    order_review(order)
    order_receipt(order)

main()

