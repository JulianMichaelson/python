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