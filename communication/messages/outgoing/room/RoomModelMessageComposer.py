import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class RoomModelMessageComposer:
    def __init__(self, model_name, room_id):
        self.response = Response(outgoing.InitialRoomInfoMessageComposer)
        self.response.write_string(model_name)
        self.response.write_int(room_id)