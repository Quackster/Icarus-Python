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

            # Sleep task
            yield coro.sleep(self.delay)
