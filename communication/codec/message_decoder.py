"""
Class for decoding messages which are received
Author: Alex (TheAmazingAussie)
"""

import game
from communication.data_streams.request import *


def parse(session, response, connection):
    """
    Parse incoming data from client
    :param session: the clients who is currently connected
    :param response: the message to parse
    :param connection: the connection
    """

    if response[0] == 60:
        session.send("<?xml version=\"1.0\"?>\r\n"
                     + "<!DOCTYPE cross-domain-policy SYSTEM \"/xml/dtds/cross-domain-policy.dtd\">\r\n"
                     + "<cross-domain-policy>\r\n"
                     + "<allow-access-from domain=\"*\" to-ports=\"*\" />\r\n"
                     + "</cross-domain-policy>\0")
    else:

        stream = Request(connection.recv(struct.unpack_from(">i", response, 0)[0]))
        message_header = stream.read_short()

        game.message_handler.incoming_message(session, message_header, stream)
