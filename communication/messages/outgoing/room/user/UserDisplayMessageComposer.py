import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class UserDisplayMessageComposer:
    def __init__(self, users):
        self.response = Response(outgoing.UserDisplayMessageComposer)
        self.response.write_int(len(users))

        for entity in users:
            self.response.write_int(entity.details.id)
            self.response.write_string(entity.details.username)
            self.response.write_string(entity.details.motto)
            self.response.write_string(entity.details.figure)
            self.response.write_int(entity.room_user.virtual_id)
            self.response.write_int(entity.room_user.position.x)
            self.response.write_int(entity.room_user.position.y)
            self.response.write_string(str(entity.room_user.position.z))
            self.response.write_int(0)
            self.response.write_int(1)
            self.response.write_string("m")
            self.response.write_int(-1)
            self.response.write_int(-1)
            self.response.write_int(0)
            self.response.write_int(1337)
            self.response.write_bool(False)