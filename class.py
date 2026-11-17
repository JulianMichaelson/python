"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""

class Pizza:
    def __init__(self, customer_name, phone_number, size, pizza, crust, drink, side):
        self.__customer_name = customer_name
        self.__phone_number = phone_number
        self.__size = size
        self.__pizza = pizza
        self.__crust = crust
        self.__drink = drink
        self.__side = side

# Getters
    def get_customer_name(self):
        return self.__customer_name

    def get_phone_number(self):
        return self.__phone_number

    def get_size(self):
        return self.__size

    def get_pizza(self):
        return self.__pizza

    def get_crust(self):
        return self.__crust

    def get_drink(self):
        return self.__drink

    def get_side(self):
        return self.__side

# Setters
    def set_customer_name(self, customer_name):
        self.__customer_name = customer_name

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def set_size(self, size):
        self.__size = size

    def set_pizza(self, pizza):
        self.__pizza = pizza

    def set_crust(self, crust):
        self.__crust = crust

    def set_drink(self, drink):
        self.__drink = drink

    def set_side(self, side):
        self.__side = side

    def return_summary(self):
        summary = (
            f"Order Summary: {self.__customer_name}, {self.__phone_number}, "
            f"{self.__size}, {self.__pizza}, {self.__crust}, "
            f"{self.__drink}, {self.__side}"
        )
        return summary

pizza_order = Pizza("Madison Carter", "779-704-1894", "Large", "Pepperoni", "Thin Crust", "Coke", "Wings")

print(pizza_order.return_summary())

pizza_order.set_size("Extra Large")
print(pizza_order.return_summary())

print(pizza_order.get_customer_name())