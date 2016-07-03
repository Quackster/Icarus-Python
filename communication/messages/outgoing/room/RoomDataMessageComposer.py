import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class RoomDataMessageComposer:
    def __init__(self, room, player, is_loading, stalking_room):
        self.response = Response(outgoing.RoomDataMessageComposer)
        self.response.write_bool(is_loading)
        room.data.serialise(self.response, is_loading)
        self.response.write_bool(stalking_room);
        self.response.write_bool(False);
        self.response.write_bool(False);
        self.response.write_bool(False);
        self.response.write_bool_int(False);
        self.response.write_bool_int(False);
        self.response.write_bool_int(False);
        self.response.write_bool(room.has_rights(player.details.id, True));
        self.response.write_int(0);
        self.response.write_int(0);
        self.response.write_int(0);
        self.response.write_int(0);
        self.response.write_int(0);