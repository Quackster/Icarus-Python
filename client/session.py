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

    def get_socket(self):
        return self.socket

    def close(self):
        """
        Force lose socket on demand
        """
        game.server.connections.remove(self)
        self.socket.close()

