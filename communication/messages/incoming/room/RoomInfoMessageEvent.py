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

        #
        # The code below prevents players being spam-joined into rooms,
        #    ie, client repetitvely sending them into the same same
        #
        # Don't ask me how this works, it's a nightmare
        #
        if room_user.is_actually_in_room():
            if room_user.room is not room:
                room_user.room.leave_room(session, True)
            else:
                forward_player = False

        if room_user.loading:
            forward_player = False

        if forward_player:
            #print ()
            session.send(RoomDataMessageComposer(room, session, message.read_int() == 1, message.read_int() == 1))