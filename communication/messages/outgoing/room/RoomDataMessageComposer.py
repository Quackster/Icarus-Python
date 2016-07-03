import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class RoomDataMessageComposer:
    def __init__(self, room, player, is_loading, check_entry):
        self.response = Response(outgoing.RoomDataMessageComposer)
        self.response.write_bool(is_loading)
        room.data.serialise(self.response, is_loading)
        self.response.write_bool(check_entry)
        self.response.write_bool(False)
        self.response.write_bool(False)
        self.response.write_bool(False)
        self.response.write_int(room.data.who_can_mute)
        self.response.write_int(room.data.who_can_kick)
        self.response.write_int(room.data.who_can_ban)
        self.response.write_bool(room.has_rights(player.details.id, True)) # is mod or owner
        self.response.write_int(0)
        self.response.write_int(0)
        self.response.write_int(0)
        self.response.write_int(0)
        self.response.write_int(0)