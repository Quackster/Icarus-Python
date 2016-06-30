"""
Room tasks
Author: Alex (TheAmazingAussie)
"""
import game
import asyncoro
from managers.room.tasks.walking_task import WalkingTask

class RoomTasks:
    def __init__(self, room):
        self.room = room
        self.tasks = [
            WalkingTask(self.room)
        ]

    def init_tasks(self):
        #while len(self.room.get_players()) > 0:
        for task in self.tasks:
            asyncoro.Coro(task.run_task)

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