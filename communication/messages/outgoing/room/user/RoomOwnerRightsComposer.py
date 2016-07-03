import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class RoomOwnerRightsComposer:
    def __init__(self, id, is_owner):
        self.response = Response(outgoing.RoomOwnerRightsComposer)
        self.response.write_int(id)
        self.response.write_bool(is_owner)