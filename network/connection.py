import asyncore
import game
from client.session import *
import communication.message_handler as message_handler


class Connection(asyncore.dispatcher_with_send):

    def new_session(self):
        """
        Add new session to the list of connected sessions
        :return:
        """
        session = Session(self)
        game.connections.append(session)

        print("Number of connections: " + str(len(game.connections)))

    def handle_read(self):
        """
        Override asyncore reading with incoming data
        :return:
        """
        data = self.recv(1024)
        session = game.async_server.find_session_by_socket(self)

        if data:
            message_handler.parse(session, data)
        else:
            session.close()
