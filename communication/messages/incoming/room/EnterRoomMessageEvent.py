import database.database_access as dao


class EnterRoomMessageEvent:
    def handle(self, session, message):

        room = dao.room_dao.get_room(message.read_int(), True)

        if room is None:
            return

        if room.in_room(session.details.id):
            return

        room.load_room(session)