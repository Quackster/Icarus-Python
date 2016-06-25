"""
Connection handler
Author: Alex (TheAmazingAussie)
"""

import asyncore
import util.logging as log
import communication.codec.message_decoder as message_decoder
import game

from managers.clients.session import Session


class Connection(asyncore.dispatcher_with_send):

    def new_session(self):
        """
        Add new clients to the list of connected sessions
        """

        try:
            session = Session(self)
            game.session_manager.connections.append(session)
        except Exception as e:
            log.error("Error caught (connection.py): " + str(e))

    def handle_read(self):
        """
        Override asyncore reading with incoming data
        """

        try:
            data = self.recv(1024)
            session = game.session_manager.find_by_socket(self)

            if data:
                message_decoder.parse(session, data)
            else:
                session.close()
        except Exception as e:
            log.error("Error caught (connection.py): " + str(e))
