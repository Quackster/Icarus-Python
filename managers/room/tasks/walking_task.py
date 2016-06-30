"""
Task to handle user walking
author: Alex
"""


class WalkingTask:
    def __init__(self, room):
        self.room = room
        self.delay = 0.5

    def run_task(self, coro=None):
        """
        Run walking task
        :param coro: generator
        :return:
        """

        # Only run when there's users in the room
        while len(self.room.get_players()) > 0:

            for entity in self.room.entities:

                room_user = entity.room_user

                if len(room_user.path) == 0:
                    continue

                if room_user.position.same_as(room_user.goal):
                    room_user.stop_walking(True)

                if room_user.is_walking and len(room_user.path) > 0:
                    next = room_user.path_cycle.next()

                    if "mv" in room_user.statuses:
                        room_user.statuses.pop("mv", None)

                    if "sit" in room_user.statuses:
                        room_user.statuses.pop("sit", None)

                    if "lay" in room_user.statuses:
                        room_user.statuses.pop("lay", None)

                    room_user.set_rotation(self.calculate_rotation(room_user.position.x, room_user.position.y, next.x, next.y), True, False)

                    height = self.room.get_model().square_height[next.x][next.y]

                    room_user.statuses["mv"] = str(next.getX()) + "," + str(next.getY()) + "," + str(height)
                    room_user.update()

                    

            # Sleep task
            yield coro.sleep(self.delay)

    def calculate_rotation(self, x1, y1, X2, Y2):
        rotation = 0
        
        if x1 > X2 and y1 > Y2:
            rotation = 7
        elif x1 < X2 and y1 < Y2:
            rotation = 3
        elif x1 > X2 and y1 < Y2:
            rotation = 5
        elif x1 < X2 and y1 > Y2:
            rotation = 1
        elif x1 > X2:
            rotation = 6
        elif x1 < X2:
            rotation = 2
        elif y1 < Y2:
            rotation = 4
        elif y1 > Y2:
            rotation = 0
        
        return rotation