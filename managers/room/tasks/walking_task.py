"""
Task to handle user walking
author: Alex
"""
import managers.pathfinder.pathfinder as pathfinder
from communication.messages.outgoing.room.user.UserStatusMessageComposer import UserStatusMessageComposer

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

            update_users = []
            for entity in self.room.entities:

                room_user = entity.room_user

                if room_user.position.same_as(room_user.goal):
                    room_user.stop_walking(False)

                if room_user.is_walking:
                    if len(room_user.path) > 0:

                        next = pathfinder.poll_first(room_user.path)

                        if "mv" in room_user.statuses:
                            room_user.statuses.pop("mv", None)

                        if "sit" in room_user.statuses:
                            room_user.statuses.pop("sit", None)

                        if "lay" in room_user.statuses:
                            room_user.statuses.pop("lay", None)

                        room_user.set_rotation(self.calculate_rotation(room_user.position.x, room_user.position.y, next.x, next.y), True, False)

                        height = self.room.get_model().square_height[next.x][next.y]

                        room_user.statuses["mv"] = str(next.x) + "," + str(next.y) + "," + str(height)
                        room_user.update_status()

                        # Update collision map
                        if not self.room.data.allow_walkthrough:
                            self.room.room_mapping.update_map(room_user.position.x, room_user.position.y, False)
                            self.room.room_mapping.update_map(next.x, next.y, True)

                        room_user.position.x = next.x
                        room_user.position.y = next.y
                        room_user.position.z = height

                    else:
                        room_user.stop_walking(True)

                elif room_user.needs_update:
                    room_user.stop_walking(False)
                    update_users.append(entity)

            if len(update_users) > 0:
                entity.room_user.room.send(UserStatusMessageComposer(update_users))

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