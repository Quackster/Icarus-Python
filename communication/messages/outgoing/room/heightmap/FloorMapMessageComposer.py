import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class FloorMapMessageComposer:
    def __init__(self, room):
        self.response = Response(outgoing.FloorMapMessageComposer)
        self.response.write_bool(True)
        self.response.write_int(room.data.wall_height)
        self.response.write_string(room.get_model().floor_map)