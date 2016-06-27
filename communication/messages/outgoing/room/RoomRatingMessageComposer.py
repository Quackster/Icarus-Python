import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class RoomRatingMessageComposer:
    def __init__(self, room_score):
        self.response = Response(outgoing.RoomRatingMessageComposer)
        self.response.write_int(room_score)
        self.response.write_bool(False)
