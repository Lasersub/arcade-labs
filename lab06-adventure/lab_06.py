import arcade

class Room:
    """
    This is a class that represents the room
    """
    def __init__(self, description, north, south, east, west):
        """ This is a method that sets up the variables in the object. """
        self.description = description  # Make sure to assign the description properly
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():
    """
    This creates the dungeon
    """
    room_list = []
    # Room 0
    room = Room("Now you are in the main hall. There's a glass door to the north and two passages to the east and the west", 3, None, 4, 1)
    room_list.append(room)
    # Room 1
    room = Room("Now you are in the west hall. There's a passage to the east or a massive stone arch to the west", None, None, 0, 2)
    room_list.append(room)
    # Room 2
    room = Room("Now you are in the coliseum. There are lots of hungry monsters, you should go back to the east", None, None, 1, None)
    room_list.append(room)
    # Room 3
    room = Room("Now you are in the balcony. You take your time to admire the surrounding landscape. Whenever you want you can come back to the south", None, 0, None, None)
    room_list.append(room)
    # Room 4
    room = Room("Now you are in the east hall. You can enter two rooms to the north and south. You can hear a holly music coming from the east. Also there's a passage to the west", 5, 6, 7, 0)
    room_list.append(room)
    # Room 5
    room = Room("Now you are in the room 1. It has a lot of pictures whose eyes are staring at your soul. You can only go south", None, 4, None, None)
    room_list.append(room)
    # Room 6
    room = Room("Now you are in the room 2. The room contains a few empty chest covered in dust and spiderwebs. You can only go north", 4, None, None, None)
    room_list.append(room)
    # Room 7
    room = Room("Now you are in the chapel. Its quartz and gold walls make you feel safe and comfortable. You can only go west", None, None, None, 4)
    room_list.append(room)

    current_room = 0
    next_room = 0


    done = False
    while not done:
        print("")
        print(room_list[current_room].description)

        direction = input("What now?\n")

        # North
        if direction.lower() == "n" or direction.lower() == "north" or direction.lower() == "norte":
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way")
                next_room = current_room
            else:
                current_room = next_room

        # South
        if direction.lower() == "s" or direction.lower() == "south" or direction.lower() == "sur":
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way")
                next_room = current_room
            else:
                current_room = next_room

        # East
        if direction.lower() == "e" or direction.lower() == "east" or direction.lower() == "este":
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way")
                next_room = current_room
            else:
                current_room = next_room

        # West
        if direction.lower() == "w" or direction.lower() == "o" or direction.lower() == "west" or direction.lower() == "oeste":
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way")
                next_room = current_room
            else:
                current_room = next_room

        # QUIT
        if direction.lower() == "q" or direction.lower() == "quit":
            print("End of the adventure")
            done = True

main()
