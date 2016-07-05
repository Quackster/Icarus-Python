"""
Room tasks
Author: Alex (TheAmazingAussie)
"""
from managers.room.tasks.walking_task import WalkingTask

class RoomTasks:
    def __init__(self, room):
        self.room = room
        self.ticked = 0
        self.tasks = {
            WalkingTask(self.room): 0.5
        }

    def start_task_cycle(self, coro=None):
        """
        Run all tasks
        :param coro: generator
        :return:
        """

        while self.room.has_reset is False:

            for event, interval in self.tasks.items():

                if interval > 0:
                    if self.ticked % interval:
                        event.do_task()
                else:
                    event.do_task()

            yield coro.sleep (0.5)

            self.ticked += 1

    def dispose(self):
        """
        Clear all task data
        :return:
        """

        self.room = None
        self.scheduler = None

        self.tasks.clear()
        self.tasks = None

        self.events.clear()
        self.events = None

        del self.room
        del self.scheduler
        del self.tasks
        del self.events