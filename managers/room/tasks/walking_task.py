"""
Task to handle user walking
author: Alex
"""
class WalkingTask:
    def __init__(self, room):
        self.room = room
        self.delay = 0.5

    def run_task(self, coro=None):

        while len(self.room.get_players()) > 0:
            print ("task run")
            yield coro.sleep(0.5)
