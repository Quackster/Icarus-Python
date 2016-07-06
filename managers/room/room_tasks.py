"""
Room tasks
Author: Alex (TheAmazingAussie)
"""
from managers.room.tasks.walking_task import WalkingTask

class RoomTasks:
    def __init__(self, room):
        self.room = room
        self.ticked = 0
        self.delay = 0.5
        self.tasks = {
            WalkingTask(self.room): 0.5
        }

    def start_cycle(self, coro=None):
        """
        Run all tasks
        :param coro: generator
        :return:
        """

        while len(self.room.get_players()) > 0:
            for event, interval in self.tasks.items():

                if interval > 0:
                    if self.ticked % interval == 0:
                        event.execute()
                else:
                    event.execute()

            self.ticked += self.delay
            yield coro.sleep (self.delay)

    def dispose(self):
        """
        Clear all task data
        :return:
        """

        del self.room
        del self.tasks
        del self.delay