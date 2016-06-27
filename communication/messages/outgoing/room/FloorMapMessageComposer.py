import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class FloorMapMessageComposer:
    def __init__(self, room):
        self.response = Response(outgoing.FloorMapMessageComposer)