"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included with assignment info.
[ ] 2. ATM runs in a loop (using a state flag or while True) to remain awake.
[ ] 3. Main menu uses match-case logic with a wildcard (case _) for selections.
[ ] 4. Inputs are validated using try-except blocks to prevent crashes.
[ ] 5. Logic prevents overdrafts and negative deposits.
[ ] 6. All currency is formatted to two decimal places (:.2f).
[ ] 7. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
account_balance = 1000.00
is_running = True
while is_running:
    print("1. Ballance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Transfer")
    print("5. Exit")
    try:
        choice = int(input("Enter the number of your selection: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    match choice:
        case 1:
            print(f"Your total balance is: ${account_balance:.2f}")
        case 2:
            try:
                withdraw_amount = float(input("How much are you withdrawing?: $"))
                if withdraw_amount <= 0:
                    print("Withdrawal more than $0")
                elif withdraw_amount > account_balance:
                    print("Withdraw within your account balance")
                else:
                    account_balance -= withdraw_amount
                    print(f"You've withdrawn ${withdraw_amount:.2f}")
            except ValueError:
                print("Enter an amount")
        case 3:
            try:
                depositing_amount = float(input("How much are you depositing?: $"))
                if depositing_amount <= 0:
                    print("Deposit more than 0$.")
                else:
                    account_balance += depositing_amount
                    print(f"You've deposited ${depositing_amount:.2f}")
                    print(f"New account ballance: ${account_balance:.2f}")
            except ValueError:
                print("Enter an amount.")
        case 4:
            try:
                transfer_amount = float(input("How much're you transferring?: $"))
                if transfer_amount <= 0:
                    print("Transfer more than $0")
                elif transfer_amount > account_balance:
                    print("Transfer within your balance")
                else:
                    account_balance -= transfer_amount
                    print(f"You've transferred ${transfer_amount:.2f}")
                    print(f"New balance: ${account_balance:.2f}")
            except ValueError:
                print("Enter an amount")
        case 5:
            print("bye!")
            is_running = False
        case _:
            print("Invalid selection")
