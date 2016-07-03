import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class RightsLevelMessageComposer:
    def __init__(self, level):
        self.response = Response(outgoing.RightsLevelMessageComposer)
        self.response.write_int(level)