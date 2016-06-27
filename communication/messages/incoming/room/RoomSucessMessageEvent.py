import database.database_access as dao

from communication.messages.outgoing.room.heightmap.FloorMapMessageComposer import *
from communication.messages.outgoing.room.heightmap.HeightMapMessageComposer import *

class RoomSuccessMessageEvent:
    def handle(self, session, message):

        room = session.room_user.room

        if room is None:
            return

        if session in room.entities:
            return

        session.send(HeightMapMessageComposer(room, room.get_model().map_size_x, room.get_model().map_size_y))
        session.send(FloorMapMessageComposer(room))
        #room_model = session.room_user.room.get_model()
        #session.send(HeightMapMessageComposer(session.room_user.room, room_model.map_size_x, room_model.map_size_y))