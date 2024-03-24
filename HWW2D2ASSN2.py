"""
1. Nested Decisions: The Adventure Game 🏰
Task 1: Code Correction
"""
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")

print()
"""
Task 2: Setting the Scene
Based on the corrected code from Task 1, expand the game. If the user chooses "cave", 
ask them if they want to "light a torch" or "proceed in the dark", and provide outcomes for each decision.
"""
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Great decision. Have fun")
    elif action == "proceed in the dark":
        print("Yikes! Be careful!")

print()
"""
Task 3: Default Path
If the user makes an invalid choice at any point, use the pass statement for now. 
Later, you can enhance this to provide feedback or a different branch of the story.
"""
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else: pass
elif place == "cave":
    action = input("light a torch or proceed in the dark? ")
    if action == "light a torch":
        print("Great decision. Have fun")
    elif action == "proceed in the dark":
        print("Yikes! Be careful!")
    else: pass
else: pass

print()
"""
2. Quick Decisions: The Event Planner 🎉
Task 1: Code Correction
"""
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue, "\n")

"""
Task 2: Venue Selection
Based on the corrected code from Task 1, further enhance the program to recommend 
additional facilities like "audio system" or "projector" based on the number of attendees.
"""
attendees = int(input("Enter number of attendees: "))
if attendees > 100:
    venue = "large hall"
    facility = "an audio system"
else:
    venue = "conference room"
    facility = "a projector"
print("We recommend using", facility, "in the", venue + ".\n")

"""
Task 3: Catering Choices
Ask the user if they want "vegetarian" food.
Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
"""
veg = (input("Would you like vegetarian food? (yes or no): "))
recommend = "Veggie Delight Caterers" if veg == 'yes' else "Gourmet Meals Caterers"
print("We recommend",recommend,"\n")
