"""
Class to store connections
Author: Alex (TheAmazingAussie)
"""

import game
from communication.messages.message_handler import MessageHandler
from managers.clients.session_manager import SessionManager
from managers.navigator.navigator_manager import NavigatorManager
from managers.room.room_manager import RoomManager

server = None
message_handler = None
session_manager = None
navigator_manager = None
room_manager = None


def init_game():
    game.session_manager = SessionManager()
    game.message_handler = MessageHandler()

    game.navigator_manager = NavigatorManager()
    game.navigator_manager.load_manager()

    game.room_manager = RoomManager()
    game.room_manager.load_manager()

