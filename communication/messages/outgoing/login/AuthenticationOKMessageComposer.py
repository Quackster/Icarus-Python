import communication.headers.outgoing as outgoing
from communication.data_handlers.response import Response


class AuthenticationOKMessageComposer:
    def __init__(self):
        self.response = Response(outgoing.AuthenticationOKMessageComposer)
