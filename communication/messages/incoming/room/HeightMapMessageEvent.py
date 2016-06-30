import database.database_access as dao


class HeightMapMessageEvent:
    def handle(self, session, message):

        room = session.room_user.room

        if room is None:
            return

        if session in room.entities:
            return

        room.load_heightmap(session)