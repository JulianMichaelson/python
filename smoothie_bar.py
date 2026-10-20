"""
-----------------------------------------------------------------------
ASSIGNMENT 9A: THE SMOOTHIE SPRINT
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Global Constants BASES and FRUITS defined as Tuples.
[ ] 3. Professional function get_price(size) returns a float.
[ ] 4. Professional function blend(size, base, fruit, scoops) for output.
[ ] 5. main() function handles try/except for scoops (int).
[ ] 6. main() calls both functions correctly.
-----------------------------------------------------------------------
"""

# GLOBAL CONSTANTS (The Pantry)
BASES = ("Water", "Apple Juice", "Orange Juice", "Milk")
FRUITS = ("Strawberry", "Banana", "Mango", "Blueberry")
SIZES  = ("Small", "Medium", "Large")

# TODO: Define get_price(size)
def get_price(size):
    if size == "Small":
        return 4.00
    elif size == "Medium":
        return 5.50
    else:
        return 7.00

# TODO: Define blend(size, base, fruit, scoops)

def blend(size, base, fruit, scoops):
    print("\n---Smoothie Order----")
    print(f"Size: {size}")
    print(f"Base: {base}")
    print(f"Fruit: {fruit}")
    print(f"Scoops: {scoops}")

# TODO: Define main() to collect input and call your logic

def main():
    print("Welcome to Julian's Smoothie Sprint")

    size = input("Sizes Small, Medium, Large): ").title().strip()
    while size not in SIZES:
        print("Choose a size for your smoothie ranging from small, medium, or large")
        size = input("Size: ").title().strip()

    fruit = input(f"Please, choose a fruit for your smoothie {FRUITS}: ").title().strip()
    base = input(f"Please choose a base for your smoothie {BASES}: ").title().strip()

    try:
        scoops= int(input("Amount of schoops: "))
    except ValueError:
        print("Enter a number of the amount of scoops you'd like ")
        return

    blend(size, base, fruit, scoops)
    price = get_price(size)
    print(f"Total Bill For The Smoothie: ${price:.2f}")

main()
