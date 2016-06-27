import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class HasOwnerRightsMessageComposer:
    def __init__(self, room):
        self.response = Response(outgoing.HasOwnerRightsMessageComposer)