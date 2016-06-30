import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class MOTDMessageComposer:
    def __init__(self, message):
        self.response = Response(outgoing.MOTDMessageComposer)
        self.response.write_int(1)
        self.response.write_string(message)