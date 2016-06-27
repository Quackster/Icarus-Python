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

        room_user = session.room_user
        room_user.virtual_id = room.get_virtual_id()

        # Add user
        room.data.users_now += 1
        room.entities.append(session)

        # Finished loading room
        room_user.loading_room = False
        room_user.in_room = True

        #room_model = session.room_user.room.get_model()
        #session.send(HeightMapMessageComposer(session.room_user.room, room_model.map_size_x, room_model.map_size_y))