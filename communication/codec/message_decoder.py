import game
from communication.messages.request import *


def parse(session, response):
    """
    Parse incoming data from client
    :param session: the session who is currently connected
    :param incoming_message: the message to parse
    :return:
    """

    if response[0] == 60:
        session.send_str("<?xml version=\"1.0\"?>\r\n"
                        + "<!DOCTYPE cross-domain-policy SYSTEM \"/xml/dtds/cross-domain-policy.dtd\">\r\n"
                        + "<cross-domain-policy>\r\n"
                        + "<allow-access-from domain=\"*\" to-ports=\"*\" />\r\n"
                        + "</cross-domain-policy>\0")
    else:

        stream = Request(response)
        message_length = stream.read_int()
        message_header = stream.read_short()

        game.message_handler.incoming_message(session, message_header, stream)
