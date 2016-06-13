import asyncore
import socket
import threading
import variables

from network.connection import *
from client.session import *

class Server(asyncore.dispatcher):

    def __init__(self, host, port):
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.set_reuse_addr()
        self.bind(('', port))
        self.listen(1)

        loop_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop")
        loop_thread.start()

    def handle_accept(self):

        pair = self.accept()

        if pair is not None:
            sock, addr = pair
            print ('Incoming connection from %s' % repr(addr))

            #session = Session(sock)
            handler = Connection(sock)
            handler.new_session()
            #variables.connections.append(Session(sock))

    def find_session_by_socket(self, socket):

        for session in variables.connections:
            if id(session.socket) == id(socket):
                return session

        return None
