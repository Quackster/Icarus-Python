"""
Session which contains socket and details
Author: Alex (TheAmazingAussie)
"""

import communication.codec.message_encoder as message_encoder
import game
from managers.clients.session_details import *
from managers.clients.session_connection import *

class Session:

    def __init__(self, socket):
        self.socket = socket
        self.connection = SessionConnection(self)
        self.details = Details()

    def send(self, data):
        self.socket.send(message_encoder.encode(data))

    def close(self):
        """
        Force lose socket on demand
        """
        game.session_manager.connections.remove(self)
        self.socket.close()

