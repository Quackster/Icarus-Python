import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class PrepareRoomMessageComposer:
    def __init__(self, room_id):
        self.response = Response(outgoing.RoomUpdateMessageComposer)
        self.response.write_int(room_id)