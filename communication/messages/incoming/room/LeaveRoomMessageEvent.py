import database.database_access as dao


class LeaveRoomMessageEvent:
    def handle(self, session, message):

        room = session.room_user.room

        if room is None:
            return

        if session not in room.entities:
            return

        room.leave_room(session, True)

        #room_model = session.room_user.room.get_model()
        #session.send(HeightMapMessageComposer(session.room_user.room, room_model.map_size_x, room_model.map_size_y))