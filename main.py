# Print a welcome screen

def welcome():
    print()
    print("Welcome to the Wizarding World! Your goal is to become an advanced")
    print("wizard by mastering all aspects of magic. You will need to learn ")
    print("spells and potions to attain your Wizard Hat. Good luck!")
    print()
    print('-'* 65)
    print()
    print("Commands: \nTo move to another room: Go 'Direction'. Example: Go North")
    print("To retrieve an item: Get 'Item'. Example: Get Wand")
    print()
    print('-'* 65)
    print()


# map
rooms = { 
    'Main Hall': { 'North' : 'Spell Room', 'West' : 'Levitation Room'},
    'Spell Room': { 'South': 'Main Hall', 'North': 'Empty Room 2', 'West': 'Potions Room', 'Item': 'Wand'},
    'Levitation Room': { 'East' : 'Main Hall', 'North': 'Potions Room', 'Item': 'Diamond'},
    'Potions Room': { 'East': 'Spell Room', 'South': 'Levitation Room', 'North': 'Empty Room 1', 'Item': 'Potion'},
    'Empty Room 1': { 'East': 'Advanced Magic Room', 'South': 'Potions Room'},
    'Empty Room 2': { 'West': 'Advanced Magic Room', 'South': 'Spell Room'},
    'Advanced Magic Room': { 'West': 'Empty Room 1', 'East': 'Empty Room 2', 'Final Item': 'Wizard Hat'}
 }

inventory = []

current_room = 'Main Hall'

welcome()

while True:
    print("You are in", current_room, "\nInventory :", inventory)
    print()
    print('-'* 65)


    if 'Item' in rooms[current_room].keys():
        print()
        print("You see a", rooms[current_room]['Item'])

    if 'Final Item' in rooms[current_room].keys():
        if len(inventory) < 3:
            print("You need to attain more skills to get the Wizard Hat. Better luck next time")
            break

        else:
            print("You have attained all the skills needed to become an advanced Wizard! Congratulations!")
            break

    print()
    move = input("What would you like to do? ").split()


    action =  move[0].title()
  
    direction = move[1].title()
    item = move[1].title()

    if action == "Go":
        try:
            current_room = rooms[current_room][direction]
            print("You travelled", direction)
            print()
            print('-'* 65)
        except:
            print("Its a dead end, try another direction")
            print()
            print('-'* 65)
            print()

    elif action == "Get":
        try:
            inventory.append(rooms[current_room]['Item'])
            print("You have attained a", rooms[current_room]['Item'])
            print()
            print('-'* 65)
            print()
            del rooms[current_room]['Item']
        except:
            print("The item you tried to pick up is not here")
            print()
            print('-'* 65)
            print()
    
    elif action == "Exit":
        break

    else:
        print("Invalid command")
        print()
        print('-'* 65)
        print()