import communication.headers.outgoing as outgoing
from communication.data_handlers.response import Response


class UserObjectMessageComposer:
    def __init__(self, details):
        self.response = Response(outgoing.UserObjectMessageComposer)
        self.response.write_int(details.id)
        self.response.write_string(details.username)
        self.response.write_string(details.figure)
        self.response.write_string("M")
        self.response.write_string(details.motto)
        self.response.write_string("")
        self.response.write_bool(False) # ?
        self.response.write_int(0) # Respect
        self.response.write_int(3) # Daily Respect Points
        self.response.write_int(3) # Daily Pet Respect Points
        self.response.write_bool(True)
        self.response.write_string("1448526834")
        self.response.write_bool(True)
        self.response.write_bool(False)