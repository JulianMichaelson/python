"""
-----------------------------------------------------------------------
ASSIGNMENT 7A: STRING MASTERY LAB
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: String Basics (Length, Indexing, ASCII) completed.
[ ] 3. Task 2: The Cleanup Crew (Strip, Case, Replace) completed.
[ ] 4. Task 3: Validation (isdigit check) completed.
[ ] 5. Task 4: The Duck Loop (.join and direct iteration) completed.
-----------------------------------------------------------------------
"""
instrument = "Acoustic Guitar"
print(instrument)
print("*" * 50)
print(len(instrument))
print(instrument[0], instrument[14])
letters = [ch for ch in instrument if ch.isalpha()]
print(min(instrument))
print(max(instrument))

messy_input = " vOLUME_knob_11 "
print(messy_input.strip().title())
print(messy_input.upper().title())
print(messy_input.replace("_", " ").title())

serial_number = "90210"
print("90210 Is Digit")
print(serial_number.isdigit())
serial_number = input("What is the serial number: ").strip()
if serial_number == "90210":
    print("Valid Serial Number")
else:
    print("Invalid Serial Number")

name_string = "Ducky"
duck_letters = list(name_string)
count = 0
for char in name_string:
    current_name = " ".join(duck_letters)
    print("There was a teacher who had a duck and Ducky was his Name-O")
    print(f"({current_name} \n)" * 3)
    print("And Ducky was his Name-O\n")
    duck_letters[count] = "🦆"
    count += 1
final_name = " ".join(duck_letters)
print(f"({final_name}) \n)" * 3)
print("And Ducky was his Name-O")