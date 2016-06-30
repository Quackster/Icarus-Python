"""
Session which contains socket and details
Author: Alex (TheAmazingAussie)
"""

import communication.codec.message_encoder as message_encoder
import game
from managers.clients.session_details import *
from managers.clients.session_connection import *
from managers.room.room_user import RoomUser

class Session:

    def __init__(self, socket):
        self.socket = socket
        self.room_user = RoomUser(self)
        self.connection = SessionConnection(self)
        self.details = Details()

    def send(self, data):
        """
        Send message to socket, this is passed through the message encoder class
        :param data: object to send
        :return:
        """
        self.socket.send(message_encoder.encode(data))

    def close(self):
        """
        Force lose socket on demand
        """

        # Leave room when disconnect
        if self.room_user.in_room():
            self.room_user.room.leave_room(self, False)

        # Remove user from list of connections
        game.session_manager.connections.remove(self)

        # Dispose user objects
        self.room_user.dispose()

        # Close socket
        self.socket.close()

