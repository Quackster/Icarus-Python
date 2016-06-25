"""
Class to store connections
Author: Alex (TheAmazingAussie)
"""

import game
from communication.messages.message_handler import MessageHandler
from managers.clients.session_manager import SessionManager
from managers.navigator.navigator_manager import NavigatorManager

#Collections
connections = []

#Instances
server = None
message_handler = None
session_manager = None
navigator_manager = None


def init_game():
    game.session_manager = SessionManager()
    game.message_handler = MessageHandler()
    game.navigator_manager = NavigatorManager()
