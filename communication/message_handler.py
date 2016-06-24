"""
Message handler
Author: Alex (TheAmazingAussie)
"""

# noinspection PyUnresolvedReferences
import util.logging as log
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
        :param message_header: the class name requested
        :param message: the rest of the message
        :return:
        """

        if message_header in self.packets:
            log.session("[MESSAGE] Handled message (" + str(incoming.__class__.__name__) + ") with header " + str(message_header))
            self.packets[message_header].handle(connection, message)
        else:
            log.session("[MESSAGE] Unhandled message header " + str(message_header) + " / " + message.get())