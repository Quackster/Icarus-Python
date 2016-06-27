import database.database_access as dao


class EnterRoomMessageEvent:
    def handle(self, session, message):

        room = dao.room_dao.get_room(message.read_int(), True)

        if room is None:
            return

        room.load_room(session)

        #room_model = session.room_user.room.get_model()
        #session.send(HeightMapMessageComposer(session.room_user.room, room_model.map_size_x, room_model.map_size_y))