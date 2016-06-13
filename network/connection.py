import asyncore
import variables
from client.session import *
import communication.message_handler as message_handler


class Connection(asyncore.dispatcher_with_send):

    session = None

    def new_session(self):
        session = Session(self)
        variables.connections.append(session)

        print("Number of connections: " + str(len(variables.connections)))

    def handle_read(self):
        data = self.recv(1024)
        session = variables.async_server.find_session_by_socket(self)

        if data:
            message_handler.parse(session, data.decode())
        else:
            session.close()
