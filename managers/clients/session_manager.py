"""
Session manager for finding users
author: TheAmazingAussie (Alex)
"""

import game


class SessionManager:

    def __init__(self):
        self.connections = []

    def find_by_socket(self, sck):
        """
        Find clients by connected socket instance
        :param socket: Asyncore socket
        """

        for session in self.connections:
            if id(session.socket) == id(sck):
                return session

    def find_by_id(self, user_id):
        """
        Find clients by connected socket instance
        :param socket: Asyncore socket
        """

        for session in self.connections:
            if session.details.id == user_id:
                return session
