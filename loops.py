"""
-----------------------------------------------------------------------
ASSIGNMENT REQUIREMENTS
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Task 1: While Loop (The Nagging Kid)
       - Repeats "Are we there yet?" until user types "yes".
       - Uses a boolean variable to control the loop.
[ ] 3. Task 2: For Loop (99 Bottles of Beer)
       - Counts backwards from 99 to 1.
       - Prints "[number] bottles of beer on the wall!"
[ ] 4. Upload to GitHub and paste the link below.
-----------------------------------------------------------------------
"""
# The Nagging Kid Assignment Portion 1
there = True

answer = input("Are we there yet? (yes or no): ")
if answer == "no":
    there = False
else:
    there = False
while not there:
        print("Are we there yet??")
        answer = input("Are we there yet?? (yes or no): ")
if answer == "yes":
    there= True

print("Yes! We're here! Now stop nagging me kid!!")
# 99 Bottles of Beer Assignment Portion 2
for bottles in range(99, 0, -1):
     print(f"{bottles} bottles of beer on the wall")





