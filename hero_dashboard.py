"""
-----------------------------------------------------------------------
ASSIGNMENT 11A: THE OFFICE HERO DASHBOARD
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global constants OFFICE_NAME and TAX_RATE defined in ALL_CAPS.
[ ] 3. Function 'process_expenses' returns TWO values (float, string).
[ ] 4. main() function uses try/except for numeric price/qty inputs.
[ ] 5. main() calls function using KEYWORD ARGUMENTS.
[ ] 6. main() correctly unpacks and prints both return values.
-----------------------------------------------------------------------
"""

OFFICE_NAME = "The Batman's Office"
TAX_RATE = 0.05

def process_expenses(item_name, price, quantity):
    """Calculate the taxed total and return it with an expense summary."""
    subtotal = price * quantity
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    summary = (
        f"{item_name} x {quantity} at ${price:.2f} each: "
        f"subtotal ${subtotal:.2f} tax ${tax:.2f}"
    )

    return total, summary

def main():
    print(f"Welcome to {OFFICE_NAME}")

    item_name = input("Enter item name: ").strip()

    try:
        price = float(input("Enter the item's price: "))
    except ValueError:
        print("Price is not valid. Price will default to $1.00.")
        price = 1.00

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("invalid quantity. Quantity will default to 1.")
        quantity = 1

    final_total, summary = process_expenses(
        item_name=item_name,
        price=price,
        quantity=quantity,
    )

    print(f"\n{summary}")
    print(f"Total included with tax: ${final_total:.2f}")


if __name__ == "__main__":
    main()