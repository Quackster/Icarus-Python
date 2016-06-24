import communication.headers.incoming as incoming
from communication.incoming.login.VersionCheckMessageEvent import *
from communication.incoming.login.AuthenticateMessageEvent import *

class MessageHandler:

    def __init__(self):
        self.packets = {
            incoming.VersionCheckMessageEvent: VersionCheckMessageEvent(),
            incoming.AuthenticateMessageEvent: AuthenticateMessageEvent()
        }

    def incoming_message(self, connection, message_header, message):
        """
        Locate the incoming message and handle it
        :param connection: the session connected
        :param header: the class name requested
        :param message: the rest of the message
        :return:
        """
        for header, instance in self.packets.items():
            if header == message_header:
                instance.handle(connection, message)