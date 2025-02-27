import arcade


class Room:
    """
    This is a class that represents the room
    """
    def __init__(self, description, north, south, east, west):
        """ This is a method that sets up the variables in the object. """
        self.description = ""
        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0

def main():
    """
    This creates the dungeon
    """
    room_list = []
    # Room 0
    room = Room ("Main hall", 3, None, 4, 1)
    room_list.append(room)
    # Room 1
    room = Room("West hall", None, None, None, 2)
    room_list.append(room)
    # Room 2
    room = Room("Coliseum", None, None, 1, None)
    room_list.append(room)
    # Room 3
    room = Room("Balcony", None, 0, None, None)
    room_list.append(room)
    # Room 4
    room = Room("East hall", 5, 6, 7, 0)
    room_list.append(room)
    # Room 5
    room = Room("Room 1", None, 4, None, None)
    room_list.append(room)
    # Room 6
    room = Room("Room 2", 4, None, None, None)
    room_list.append(room)
    # Room 7
    room = Room("Chapel", None, None, None, 6)
    room_list.append(room)

    current_room = 0
    print(room_list[current_room])

main()