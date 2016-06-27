"""
Room model data
Author: Alex (TheAmazingAussie)
"""

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

        self.squares = [[0 for i in range(0, self.map_size_y)] for j in range(0, self.map_size_x)]
        self.squareHeight = [[0 for i in range(0, self.map_size_y)] for j in range(0, self.map_size_x)]
        self.squareChar = [[0 for i in range(0, self.map_size_y)] for j in range(0, self.map_size_x)]

        for y in range(0, self.map_size_y):

            if y > 0:
                temporary[y] = temporary[y][1:] # Substring 1

            for x in range (0, self.map_size_x):
                square = temporary[y][x:x + 1].strip()

                if square == "x":
                    self.squares.append(x)
                    self.squares[x][y] = CLOSED
                elif self.is_numeric(square):
                    self.squares[x][y] = OPEN
                    self.squareHeight[x][y] = float(square)

                if self.door_x == x and self.door_y == y:
                    self.squares[x][y] = OPEN
                    self.squareHeight[x][y] = float(self.door_z)

                self.squareChar[x][y] == square

        string_builder = ""

        for i in range(0, self.map_size_y):
            for j in range (0, self.map_size_x):

                try:
                    if j == self.door_x and i == self.door_y:
                        string_builder += str(self.door_z)
                    else:
                        string_builder += self.squareChar[x][y]
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