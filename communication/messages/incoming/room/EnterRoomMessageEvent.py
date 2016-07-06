import database.database_access as dao


class EnterRoomMessageEvent:
    def handle(self, session, message):

        room = dao.room_dao.get_room(message.read_int(), True)

        if room is None:
            return

        if session.room_user.room is not None:
            session.room_user.room.leave_room(session, False)

        room.load_room(session)