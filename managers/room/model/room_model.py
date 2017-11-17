"""
Room model data
Author: Alex (TheAmazingAussie)
"""

from managers.pathfinder.point import Point

OPEN = 0
CLOSED = 1


class RoomModel:
    def __init__(self, name, heightmap, door_x, door_y, door_z, door_rotation):
        self.name = name
        self.heightmap = heightmap
        self.door_x = door_x
        self.door_y = door_y
        self.door_z = door_z
        self.door_rotation = door_rotation

        temporary = self.heightmap.split("{13}")

        self.map_size_x = len(temporary[0])
        self.map_size_y = len(temporary)

        self.squares = self.get_2d_array(CLOSED)
        self.square_height = self.get_2d_array(CLOSED)
        self.square_char = self.get_2d_array(CLOSED)

        for y in range(0, self.map_size_y):

            if y > 0:
                temporary[y] = temporary[y][1:] # Substring 1

            for x in range (0, self.map_size_x):
                square = temporary[y][x:x + 1].strip().lower()

                if square == "x":
                    self.squares.append(x)
                    self.squares[x][y] = CLOSED

                elif self.is_numeric(square):
                    self.squares[x][y] = OPEN
                    self.square_height[x][y] = int(RoomModel.parse(square))

                if self.door_x == x and self.door_y == y:
                    self.squares[x][y] = OPEN
                    self.square_height[x][y] = int(self.door_z)

                self.square_char[x][y] = square

        string_builder = ""

        for y in range(0, self.map_size_y):
            for x in range (0, self.map_size_x):

                try:
                    if x == self.door_x and y == self.door_y:
                        string_builder += str(self.door_z)
                    else:
                        string_builder += self.square_char[x][y]
                except Exception as e:
                    string_builder += "0"

            string_builder += chr(13)

        self.floor_map = string_builder
        
    def parse(square):

        if square == "0":
            return 0
        if square == "1":
            return 1
        if square == "2":
            return 2
        if square == "3":
            return 3
        if square == "4":
            return 4
        if square == "5":
            return 5
        if square == "6":
            return 6
        if square == "7":
            return 7
        if square == "8":
            return 8
        if square == "9":
            return 9
        if square == "a":
            return 10
        if square == "b":
            return 11
        if square == "c":
            return 12
        if square == "d":
            return 13
        if square == "e":
            return 14
        if square == "f":
            return 15
        if square == "g":
            return 16
        if square == "h":
            return 17
        if square == "i":
            return 18
        if square == "j":
            return 19
        if square == "k":
            return 20
        if square == "l":
            return 21
        if square == "m":
            return 22
        if square == "n":
            return 23
        if square == "o":
            return 24
        if square == "p":
            return 25
        if square == "q":
            return 26
        if square == "r":
            return 27
        if square == "s":
            return 28
        if square == "t":
            return 29
        if square == "u":
            return 30
        if square == "v":
            return 31
        if square == "w":
            return 32

        return -1

    def is_numeric(self, square):
        try:
            number = float(square)
            return True
        except Exception as e:
            return False

    def get_2d_array(self, data_type=None):
        return [[data_type for y in range(-1, self.map_size_y)] for x in range(-1, self.map_size_x)]

    def get_door_point(self):
        return Point(self.door_x, self.door_y, self.door_z)
