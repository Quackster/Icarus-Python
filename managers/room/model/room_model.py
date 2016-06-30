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

        temporary = self.heightmap.split(chr(13))

        self.map_size_x = len(temporary[0])
        self.map_size_y = len(temporary)

        self.squares = self.get_2d_array()
        self.square_height = self.get_2d_array()
        self.square_char = self.get_2d_array()

        for y in range(0, self.map_size_y):

            if y > 0:
                temporary[y] = temporary[y][1:] # Substring 1

            for x in range (0, self.map_size_x):
                square = temporary[y][x:x + 1].strip().lower()
                self.squares[x][y] = CLOSED

                if square == "x":
                    self.squares.append(x)
                    self.squares[x][y] = CLOSED
                elif self.is_numeric(square):
                    self.squares[x][y] = OPEN
                    self.square_height[x][y] = float(square)

                if self.door_x == x and self.door_y == y:
                    self.squares[x][y] = OPEN
                    self.square_height[x][y] = float(self.door_z)

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

    def is_numeric(self, input):
        try:
            number = float(input)
            return True
        except Exception as e:
            return False

    def get_2d_array(self):
        return [[CLOSED for y in range(0, self.map_size_y)] for x in range(0, self.map_size_x)]

    def get_door_point(self):
        return Point(self.door_x, self.door_y, self.door_z)