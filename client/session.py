"""
Session which contains socket and details
Author: Alex (TheAmazingAussie)
"""

import game
import communication.codec.message_encoder as message_encoder
from client.details import *


class Session:

    def __init__(self, socket):
        self.socket = socket
        self.details = Details()

    def send(self, data):
        self.socket.send(message_encoder.encode(data))

    def close(self):
        """
        Force lose socket on demand
        """
        game.session_manager.connections.remove(self)
        self.socket.close()

