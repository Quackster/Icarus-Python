import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class NavigatorPreferencesComposer:
    def __init__(self):

        self.response = Response(outgoing.NavigatorPreferencesComposer)
        self.response.write_int(50)
        self.response.write_int(50)
        self.response.write_int(580)
        self.response.write_int(600)
        self.response.write_bool_int(True)
        self.response.write_int(1)
