"""
Class to store connections
Author: Alex (TheAmazingAussie)
"""

import game
from communication.messages.message_handler import MessageHandler
from managers.clients.session_manager import SessionManager

#Collections
connections = []

#Instances
server = None
message_handler = None
session_manager = None


def init_game():
    game.session_manager = SessionManager()
    game.message_handler = MessageHandler()
