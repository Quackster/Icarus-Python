import asyncore
import variables
from client.session import *
import communication.message_handler as message_handler


class Connection(asyncore.dispatcher_with_send):

    def new_session(self):
        """
        Add new session to the list of connected sessions
        :return:
        """
        session = Session(self)
        variables.connections.append(session)

        print("Number of connections: " + str(len(variables.connections)))

    def handle_read(self):
        """
        Override asyncore reading with incoming data
        :return:
        """
        data = self.recv(1024)
        session = variables.async_server.find_session_by_socket(self)

        if data:
            message_handler.parse(session, data.decode())
        else:
            session.close()
