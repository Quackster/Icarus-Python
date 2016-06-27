"""
Request room info
Author: Alex (TheAmazingAussie)
"""

import database.database_access as dao
from communication.messages.outgoing.room.RoomDataMessageComposer import RoomDataMessageComposer

class RoomInfoMessageEvent:
    def handle(self, session, message):
        """
        Send room_dao info when requested
        :param session: the clients who requests RoomInfoMessageEvent handler
        :param message: the incoming message
        """

        room = dao.room_dao.get_room(message.read_int(), True)

        if room is None:
            return

        room_user = session.room_user
        forward_player = True

        if room_user.in_room:
            if room_user.room is not room:
                ## Leave room_dao
                print ("leave room_dao")
            else:
                forward_player = False

        if room_user.is_loading_room:
            forward_player = False

        if forward_player:
            session.send(RoomDataMessageComposer(room, session, message.read_int() == 1, message.read_int() == 1))