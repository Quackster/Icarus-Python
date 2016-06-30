import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class UserStatusMessageComposer:
    def __init__(self, users):
        self.response = Response(outgoing.UserStatusMessageComposer)
        self.response.write_int(len(users))

        for entity in users:
            self.response.write_int(entity.room_user.virtual_id)
            self.response.write_int(entity.room_user.position.x)
            self.response.write_int(entity.room_user.position.y)
            self.response.write_string(str(entity.room_user.position.z))
            self.response.write_int(entity.room_user.head_rotation)
            self.response.write_int(entity.room_user.rotation)

            status = "/"

            for key, value in entity.room_user.statuses.items():
                status += key + " " + value + "/"

            self.response.write_string(status + "/")