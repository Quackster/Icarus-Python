"""
Connection handler
Author: Alex (TheAmazingAussie)
"""

import asyncore
import communication.codec.message_decoder as message_decoder
import game
from client.session import *


class Connection(asyncore.dispatcher_with_send):

    def new_session(self):
        """
        Add new session to the list of connected sessions
        """

        session = Session(self)
        game.get_connections().append(session)

    def handle_read(self):
        """
        Override asyncore reading with incoming data
        """

        data = self.recv(1024)
        session = game.server.find_session_by_socket(self)

        if data:
            message_decoder.parse(session, data)
        else:
            session.close()
