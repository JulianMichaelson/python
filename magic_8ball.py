"""
-----------------------------------------------------------------------
ASSIGNMENT 7B: THE MAGIC 8 BALL
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. RESPONSES is a tuple containing at least 8 string options.
[ ] 3. Program uses a 'while True' loop to keep the game running.
[ ] 4. random.choice() selects the answer from the tuple.
[ ] 5. Logic checks if "quit" is in the user input to break the loop.
-----------------------------------------------------------------------
"""
import random

# TODO: Create a tuple of at least 8 responses
RESPONSES = ("Yes", "No", "Maybe", "Ask again later", "Without a doubt", "Don't count on it", "Better not to tell you now", "Most likely" "Hell no")

print("Welcome to the Digital Oracle!")
while True:
    QUESTION = input("Enter your question or enter quit to leave: ").strip()
    if QUESTION.lower() == "quit":
        print("Goodbye")
        break
    print(random.choice(RESPONSES))

# TODO: Create a while loop that keeps asking questions
# TODO: Use random.choice(RESPONSES) to answer
# TODO: If user types "quit", break the loop