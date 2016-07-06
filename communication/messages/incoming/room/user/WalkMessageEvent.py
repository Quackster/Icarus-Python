import managers.pathfinder.pathfinder as pathfinder

class WalkMessageEvent:
    def handle(self, session, message):

        x = message.read_int()
        y = message.read_int()

        room_user = session.room_user

        room_user.goal.x = x
        room_user.goal.y = y

        path_list = pathfinder.make_path(room_user.position, room_user.goal, room_user.room)

        room_user.path = path_list
        room_user.is_walking = True