"""
-----------------------------------------------------------------------
ASSIGNMENT 6A: TICKET SALES
-----------------------------------------------------------------------
[ ] 1. Create a list of 20 seats (numbered 1-20).
[ ] 2. Display the list of available seats.
[ ] 3. Ask user for a seat number (0 to quit).
[ ] 4. Remove the selected seat from the list.
[ ] 5. Handle invalid inputs (seat taken or doesn't exist).
[ ] 6. Repeat until user quits or seats are empty.
-----------------------------------------------------------------------
"""
available_seats = list(range(1, 21))
print("Select your seat, please")
print("available seats:", available_seats)

while True:
    if not available_seats:
        print("There are no more seats available, sorry")
        break

    seat_selection = input("Enter an available seat. If you'd like to back out from picking a seat, pick 0: ").strip()

    if seat_selection == "0":
        print("Thank you for coming to the movies, have a good night and goodbye")
        break

    if not seat_selection.isdigit():
        print("Invalid. Enter a seat number from 1-20 or put 0 to exit")
        continue

    seat = int(seat_selection)

    if seat < 1 or seat > 20:
        print("We do not have that desired seat. Please choose a seat from 1 to 20.")
        continue

    if seat not in available_seats:
        print("That seat has already been purchased. Please choose another seat.")
        continue

    available_seats.remove(seat)
    print(f"Seat {seat} has now been picked.")
    print("Available seats:", available_seats)