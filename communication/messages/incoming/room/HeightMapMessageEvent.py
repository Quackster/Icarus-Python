"""
Load heightmap and furniture/AI data for room
Author: Alex (TheAmazingAussie)
"""


class HeightMapMessageEvent:
    def handle(self, session, message):

        room = session.room_user.room

        if room is None:
            return

        if session in room.entities:
            return

        room.load_heightmap(session)