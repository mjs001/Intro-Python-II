from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].w = room['foyer']
room['foyer'].a = room['outside']
room['foyer'].s = room['overlook']
room['foyer'].d = room['narrow']
room['overlook'].w = room['foyer']
room['narrow'].a = room['foyer']
room['narrow'].s = room['treasure']
room['treasure'].d = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def __init__(self, name, current_rm):
    self.name = name
    self.current_rm = current_rm

    def __str__(self):
        return f"<Human '{self.name}' is currently located {self.current_rm}>"

    playerTest = ("Myco", "Outside")
    print(playerTest)

    while True:
        print(playerTest)
        print("Enter Direction")
        print("To add items to inventory: take <item-name>")
        print("To remove item from inventory: remove <item-name>")
        direction = direction.strip().lower().split(" ")
        if len(response) == 1:
            if direction not in ["w", "a", "s", "d", "q"]:
                print("Not a valid direction!")
                continue
        if direction == "q":
            print("EXITING")
            break
        current_rm = playerTest.current_rm
        if direction == "w":
            if current_rm.w is None:
                print("The player is stuck!")
                continue
            else:
                playerTest.current_rm = current_rm.w
        elif direction == "a":
                if current_rm.a is None:
                    print("The player is stuck!")
                else:
                    playerTest.current_rm = current_rm.a 
        elif direction == "S":
                if current_rm.s is None:
                    print("The player is stuck!")
                else:
                    playerTest.current_rm = current_rm.s 
        elif direction == "d":
            if current_rm.d is None:
                print("The player is stuck!")
            else:
                playerTest.current_rm = current_rm.d
        elif len(response) == 2:
            print(len(response))

            #START HERE TOMORROW