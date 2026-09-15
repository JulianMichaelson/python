person1 = "Julian"
person2 = "Madison"
person3 = "Marley"

action_walks_away = 1
action_jumps_in = 2
action_throws_a_rock = 3
action_kicks_him = 4
action_runs_in_circles = 5
action_punches_him = 6

print(f"{person1} is out on the road, driving to pick up and hangout with his girlfriend, {person2}")
print(f"{person1} Arrives at {person2}'s house and she enters the car.")
print(f"{person1} and {person2} drive to the park and come across {person1}'s enemy, {person3}.")
print(f"{person1} gets attacked by {person3}. The two begin fighting {person2} is just watching--unsure")
print("-" * 40)

print(f"What should {person2} do?")
choice_1 = int(input("Choose an action from 1-6: "))
if choice_1 == action_walks_away or choice_1 == action_runs_in_circles:
    print(f"{person2} Isn't much help, really")
    print(f"{person1} says: 'Madison! What are you doing?'")
elif choice_1 == action_jumps_in:
    choice_2 = int(input("What should Madison do next? "))
    if choice_2 == action_punches_him:
        print(f"{person3} Can't handle it and runs away")
        print(f"{person3} says: 'I'll get you two next time!'")
elif choice_1 == action_kicks_him:
    print(f"{person2} Has decided it's soccer time")
elif choice_1 == action_throws_a_rock:
    print(f"{person2} Has decided it's football time")
elif not (choice_1 >= 1 and choice_1 <= 6):
    print(f"{person1} says: Madison come back and help me!")
else:
    print(f"She comes back and {person3} is confused")
print("-" * 40)