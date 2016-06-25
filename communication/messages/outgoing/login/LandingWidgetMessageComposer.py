import communication.headers.outgoing as outgoing
from communication.data_handlers.response import Response


class LandingWidgetMessageComposer:
    def __init__(self):
        self.response = Response(outgoing.LandingWidgetMessageComposer)
        self.response.write_string("")
        self.response.write_string("")
