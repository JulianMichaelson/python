"""
-----------------------------------------------------------------------
ASSIGNMENT 6B: THE DEPARTMENT SECURITY TERMINAL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Department constant defined in ALL_CAPS.
[ ] 3. Username tuple and password list defined.
[ ] 4. While loop runs interactively.
[ ] 5. Try/except catches TypeError and tells user to email help desk.
-----------------------------------------------------------------------
"""
DEPARTMENT = "ELROY"
USER_NAMES = ("Elvis", "Roy", "Shiba")
passwords = ["Elvis123", "Roy456", "Shiba789"]

print(f"You are currently at the {DEPARTMENT} security terminal.")

while True:
    print("\n1. Username Search")
    print("2. Change Username")
    print("3. Change Password")
    print("4. Exit")

    choice = input("Choose from the available options: ").strip()

    if choice == "1":
        Username = input("Username you're searching: ").strip()

        try:
            index = USER_NAMES.index(Username)
            print(f"{Username} is in the system.")
            print(f"Password: {passwords[index]}")
        except ValueError:
            print("That username was not found within the system.")
        except IndexError:
            print("The usernames and passwords do not match, they're incorrect.")

    elif choice == "2":
        username = input("Username to change: ").strip()

        try:
            index = USER_NAMES.index(Username)
            new_username = input("New username: ").strip()
            USER_NAMES[index] = new_username
        except ValueError:
            print("That username was not found.")
        except TypeError:
            print("the username is unable to be changed. For assistance, please email the help desk, thank you.")
        except IndexError:
            print("That index is not available.")

    elif choice == "3":
        username = input("Whose password do you want to change? ").strip()

        try:
            index = USER_NAMES.index(Username)
            passwords[index] = input("New password: ").strip()
            print("Password has been successfully updated")
        except ValueError:
            print("The Username was not found in our system")
        except IndexError:
            print("That username is not available")

    elif choice == "4":
        print("Goodbye!.")
        break
    else:
        print("Please choose 1, 2, 3 and 4")