from room import Room
from player import Player
from item import Item

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player("Player1", room['outside'])

room['outside'].players.append(player1)
room['outside'].items.append(Item("Dagger", "Small blade"))
room['outside'].items.append(Item("Scroll", "Map To Castle"))

room['foyer'].items.append(Item("Jar of Ooze", "Magic?"))
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

key_input = ""
current_room = ""

while key_input != "q":

    for r in room:
        if player1 in room[r].players:
            print("{}: {}".format(
                room[r].name, room[r].description))
            room[r].print_contents()
            player1.print_inventory()
            current_room = r

    key_input = input(
        "Enter a direction [n, e, s, w] or a command [grab <item>]: ")
    print("\n")

    if key_input == "n":
        if not hasattr(room[current_room], 'n_to'):
            print("Can't move north\n")
        else:
            room[current_room].players.remove(player1)
            room[current_room].n_to.players.append(player1)
            current_room = room[current_room].n_to

    elif key_input == "e":
        if not hasattr(room[current_room], 'e_to'):
            print("Can't move east\n")
        else:
            room[current_room].players.remove(player1)
            room[current_room].e_to.players.append(player1)
            current_room = room[current_room].e_to

    elif key_input == "s":
        if not hasattr(room[current_room], 's_to'):
            print("Can't move south\n")
        else:
            room[current_room].players.remove(player1)
            room[current_room].s_to.players.append(player1)
            current_room = room[current_room].s_to

    elif key_input == "w":
        if not hasattr(room[current_room], 'w_to'):
            print("Can't move west\n")
        else:
            room[current_room].players.remove(player1)
            room[current_room].w_to.players.append(player1)
            current_room = room[current_room].w_to
    elif "grab" in key_input:
        parse = key_input.split()
        item_to_grab = parse[1]

        found = False
        for item in room[current_room].items:
            if item.name == item_to_grab:
                room[current_room].items.remove(item)
                player1.grab(item)
                found = True
                break

        if not found:
            input("%s doesn't exist" % (item_to_grab))
