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
        game.session_manager.connections.remove(self)
        self.socket.close()
        self.room_user.dispose()

