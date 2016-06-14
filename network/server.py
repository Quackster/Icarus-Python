import asyncore
import socket
import threading
import game

from network.connection import *
from client.session import *

class Server(asyncore.dispatcher):

    def __init__(self, host, port):
        """
        Create asyncore socket with defined host and port
        :param host: the host/ip address to listen on, '' for all potential IP addresses
        :param port: the port the socket should listen on
        :return:
        """
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.set_reuse_addr()
        self.bind(('', port))
        self.listen(1)

        loop_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop")
        loop_thread.start()

    def handle_accept(self):
        """
        Override accept handling
        :return:
        """

        pair = self.accept()

        if pair is not None:
            sock, addr = pair
            print ('Incoming connection from %s' % repr(addr))

            #session = Session(sock)
            handler = Connection(sock)
            handler.new_session()
            #variables.connections.append(Session(sock))

    def find_session_by_socket(self, socket):
        """
        Find session by connected socket instance
        :param socket: Asyncore socket
        :return:
        """
        for session in game.connections:
            if id(session.socket) == id(socket):
                return session

        return None
