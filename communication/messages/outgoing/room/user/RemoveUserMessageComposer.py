import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class RemoveUserMessageComposer:
    def __init__(self, virtual_id):
        self.response = Response(outgoing.UserLeftRoomMessageComposer)
        self.response.write_string(str(virtual_id))