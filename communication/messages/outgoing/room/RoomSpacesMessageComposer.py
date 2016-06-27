import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class RoomSpacesMessageComposer:
    def __init__(self, space, data):
        self.response = Response(outgoing.RoomSpacesMessageComposer)
        self.response.write_string(space)
        self.response.write_string(data)
