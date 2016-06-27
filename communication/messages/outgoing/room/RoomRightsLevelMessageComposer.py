import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class RoomRightsLevelMessageComposer:
    def __init__(self, level):
        self.response = Response(outgoing.RoomRightsLevelMessageComposer)
        self.response.write_int(level)