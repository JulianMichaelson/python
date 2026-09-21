"""
-----------------------------------------------------------------------
ASSIGNMENT 5A: INPUT VALIDATION
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. All 5 inputs have 'while' loop validation.
[ ] 3. The more tickets loop uses .upper() and correct Boolean logic.
[ ] 4. Include a try and except statement around the entire program. Should have one defined 
       exception (probably value error) and a generic exception
[ ] 5. Have pinned a variable in the WATCH window and took a screenshot.
-----------------------------------------------------------------------
Create a registration form (registration.py) in which each input is validated using a while loop.  Registration for a dance:
Requirements:

First Name & Last Name: Cannot be blank.
Age: Must be a number; also check whether they are older or younger than 21 to determine whether they get a drink ticket.
Phone Number: Cannot be blank.
Ticket Count: Must be a valid integer > 0 (Crash-Proof!).
Additional Tickets? (Y/N)
"""
try:
    first_name = input("Enter Your First Name: ")
    while first_name == "":
        print("Error: Name cannot be empty")
        first_name = input("Please enter your First Name: ")

    last_name = input("Enter your Last Name: ")
    while last_name == "":
        print("Error: Name cannot be empty")
        last_name = input("Please enter your Last Name: ")

    age = input("Please state your age: ")
    while not age.isdigit():
        print("Please state your age--Age should be in digits")
        age = input("Please state your age: ")
    age = int(age)

    if age >= 21:
        drink_ticket = "Yes"
    else:
        drink_ticket = "No"

    print(f"Drink Ticket: {drink_ticket}")
    phone_number = input("Please enter your phone number: ")
    while phone_number == "":
        print("Your phone number cannot be empty.")
        phone_number = input("Please Enter your phone number: ")

    ticket_count = input("How many tickets would you like to buy?: ")
    while not ticket_count.isdigit() or int(ticket_count) <= 0:
        print("Ticket count cannot be 0.")
        ticket_count = input("How many tickets would you like to buy?:")
    ticket_count = int(ticket_count)

    additional_tickets = input("Are you getting any additional tickets? Y/N:").upper()
    while additional_tickets not in ("Y", "N"):
        print("Respond Y or N")
        additional_tickets = input("Are you getting any additional tickets? Y/N:").upper()

except ValueError:
    print("A value error occurred.")

except Exception:
    print("An unexpected error occurred.")

finally:
    print(f"\n Registration Complete for {first_name}!")