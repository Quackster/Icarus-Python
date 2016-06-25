import communication.headers.outgoing as outgoing
from communication.data_handlers.response import Response


class UniqueMachineIDMessageComposer:
    def __init__(self, unique_id):
        self.response = Response(outgoing.UniqueMachineIDMessageComposer)
        self.response.write_string(unique_id)
