from util.bytestream import *
import util.logging as log
import game


def parse(session, response):
    """
    Parse incoming data from client
    :param session: the session who is currently connected
    :param incoming_message: the message to parse
    :return:
    """

    if response[0] == 60:
        session.send("<?xml version=\"1.0\"?>\r\n"
                        + "<!DOCTYPE cross-domain-policy SYSTEM \"/xml/dtds/cross-domain-policy.dtd\">\r\n"
                        + "<cross-domain-policy>\r\n"
                        + "<allow-access-from domain=\"*\" to-ports=\"*\" />\r\n"
                        + "</cross-domain-policy>\0")
    else:

        stream = ByteStream(response)
        message_length = stream.read_int()
        message_header = stream.read_short()

        print ("Received: " +  str(message_header) + " / " + response.decode("ISO-8859-1")[4:])

        game.messages.incoming_message(session, message_header, stream)
