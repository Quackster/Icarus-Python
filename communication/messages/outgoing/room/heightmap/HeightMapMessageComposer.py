import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class HeightMapMessageComposer:
    def __init__(self, room, map_size_x, map_size_y):

        print (type(map_size_x))

        self.response = Response(outgoing.HeightMapMessageComposer)
        self.response.write_int(map_size_x)
        self.response.write_int(map_size_x * map_size_y)

        for y in range(0, map_size_y):
            for x in range(0, map_size_x):

                self.response.write_short(int(room.get_model().square_height[x][y] * 256))