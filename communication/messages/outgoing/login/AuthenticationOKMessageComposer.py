import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class AuthenticationOKMessageComposer:
    def __init__(self):
        self.response = Response(outgoing.AuthenticationOKMessageComposer)
