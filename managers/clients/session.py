"""
Session which contains socket and details
Author: Alex (TheAmazingAussie)
"""

import communication.codec.message_encoder as message_encoder
import game
from managers.clients.session_details import *
from managers.room.room_user import RoomUser

class Session:

    def __init__(self, socket):
        self.socket = socket
        self.room_user = RoomUser(self)
        self.details = Details()
        self.disposed = False

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

        # Character is disposed, don't use if disposed - else you'll fuckup the whole server you dumb cunt! :o
        self.disposed = True

        # Remove user from list of connections
        game.session_manager.connections.remove(self)

        # Leave room when disconnect
        if self.room_user.in_room():
            self.room_user.room.leave_room(self, False, False)

        # Dispose all rooms if we can
        for room in game.room_manager.get_player_rooms(self.details.id):
            room.dispose(False)

        # Dispose user objects
        self.room_user.dispose()

        # Close socket
        self.socket.close()

