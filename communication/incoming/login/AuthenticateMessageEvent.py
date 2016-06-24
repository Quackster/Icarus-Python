"""
Authenticate user class using received SSO ticket
Author: Alex (TheAmazingAussie)
"""

import util.logging as log
import communication.headers.outgoing as outgoing
from communication.messages.response import *


class AuthenticateMessageEvent:
    def handle(self, session, message):
        """
        Handle sso request
        :param session: the session who requests AuthenticateMessageEvent handler
        :param message: the incoming message with login details
        """

        log.session("SSO ticket: " + message.read_string())

        response = Response(outgoing.AuthenticationOKMessageComposer)
        session.send(response)

        response = Response(outgoing.HomeRoomMessageComposer)
        response.write_int(0)
        response.write_int(0)
        session.send(response)

        response = Response(outgoing.LandingWidgetMessageComposer)
        response.write_string("")
        response.write_string("")
        session.send(response)