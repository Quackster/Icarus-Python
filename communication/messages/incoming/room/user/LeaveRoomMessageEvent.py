"""
Leave room event
Author: Alex (TheAmazingAussie)
"""


class LeaveRoomMessageEvent:
    def handle(self, session, message):

        room = session.room_user.room

        if room is None:
            return

        if not room.in_room(session.details.id):
            return

        room.leave_room(session, True)

        #room_model = session.room_user.room.get_model()
        #session.send(HeightMapMessageComposer(session.room_user.room, room_model.map_size_x, room_model.map_size_y))