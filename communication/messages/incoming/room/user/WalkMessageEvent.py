from managers.pathfinder.pathfinder import *

class WalkMessageEvent:
    def handle(self, session, message):

        x = message.read_int()
        y = message.read_int()

        room_user = session.room_user

        room_user.goal.x = x
        room_user.goal.y = y

        astar = AStar(room_user.room.get_model().get_node_array())
        room_user.path = astar.search(room_user.position, room_user.goal)

        print (room_user.path)
