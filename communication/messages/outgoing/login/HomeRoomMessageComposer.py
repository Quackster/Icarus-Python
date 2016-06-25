import communication.headers.outgoing as outgoing
from communication.data_handlers.response import Response


class HomeRoomMessageComposer:
    def __init__(self, room_id, force_enter):
        self.response = Response(outgoing.HomeRoomMessageComposer)
        self.response.write_int(room_id)
        self.response.write_bool_int(force_enter)
