"""
Message handler
Author: Alex (TheAmazingAussie)
"""

# noinspection PyUnresolvedReferences
from communication.messages.incoming.login.VersionCheckMessageEvent import *
from communication.messages.incoming.login.AuthenticateMessageEvent import *
from communication.messages.incoming.login.UniqueIDMessageEvent import *

from communication.messages.incoming.user.CurrencyBalanceMessageEvent import *
from communication.messages.incoming.user.InfoRetrieveMessageEvent import *

import communication.headers.incoming as incoming
import util.logging as log


class MessageHandler:

    def __init__(self):
        self.packets = {
            incoming.VersionCheckMessageEvent: VersionCheckMessageEvent(),
            incoming.AuthenticateMessageEvent: AuthenticateMessageEvent(),
            incoming.UniqueIDMessageEvent: UniqueIDMessageEvent(),

            # User
            incoming.GetCurrencyBalanceMessageEvent: CurrencyBalanceMessageEvent(),
            incoming.InfoRetrieveMessageEvent: InfoRetrieveMessageEvent()
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
            log.session("[MESSAGE] Handled message with header " + str(message_header) + " / " + message.get_message_as_string())
            self.packets[message_header].handle(connection, message)
        else:
            log.session("[MESSAGE] Unhandled message header " + str(message_header) + " / " + message.get_message_as_string())