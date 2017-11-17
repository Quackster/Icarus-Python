import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class AvailabilityMessageComposer:
    def __init__(self):
        self.response = Response(outgoing.AvailabilityMessageComposer)
        self.response.write_bool(True)
        self.response.write_bool(False)
        self.response.write_bool(True)
