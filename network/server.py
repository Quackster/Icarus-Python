"""
Server using asyncore
Author: Alex (TheAmazingAussie)
"""

# noinspection PyUnresolvedReferences
import asyncore
# noinspection PyUnresolvedReferences
import game
import socket
import threading
from network.connection import *


class Server(asyncore.dispatcher):
    def __init__(self, host, port):
        """
        Create asyncore socket with defined host and port
        :param host: the host/ip address to listen on, '' for all potential IP addresses
        :param port: the port the socket should listen on
        """
        asyncore.dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.set_reuse_addr()
        self.bind(('', port))
        self.listen(1)

        loop_thread = threading.Thread(target=asyncore.loop, name="Asyncore Loop")
        loop_thread.start()

    def handle_accepted(self, sock, addr):
        """
        Override accept handling
        """
        #print ('Incoming connection from %s' % repr(addr))
        handler = Connection(sock)
        handler.new_session()

