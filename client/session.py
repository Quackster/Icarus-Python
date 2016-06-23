import game
from client.details import *

class Session:
    def __init__(self, socket):
        self.socket = socket
        self.details = Details()

    def send(self, data):
        self.socket.send(data.encode())

    def close(self):
        """
        Force lose socket on demand
        :return:
        """
        game.connections.remove(self)
        self.socket.close()

