"""
Authenticate user class using received SSO ticket
Author: Alex (TheAmazingAussie)
"""

import util.logging as log
import communication.headers.outgoing as outgoing
import database.dao as dao
from communication.messages.response import *


class AuthenticateMessageEvent:
    def handle(self, session, message):
        """
        Handle sso request
        :param session: the session who requests AuthenticateMessageEvent handler
        :param message: the incoming message with login details
        """
        sso_ticket = message.read_string()

        log.session("SSO ticket: " + sso_ticket)

        if not dao.user.authenticate(session, sso_ticket):
            print ("Invalid sso ticket, kicking user")
            session.close()
            return

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

        response = Response(outgoing.UserObjectMessageComposer)
        response.write_int(1)
        response.write_string("Alex")
        response.write_string("hr-676-45.hd-207-10.ch-266-.lg-281-63.sh-906-71.ha-1005-83.ea-1403-70.ca-1812-")
        response.write_string("M")
        response.write_string("I eat cake everyday, m8")
        response.write_string("")
        response.write_bool(False)
        response.write_int(0)
        response.write_int(3)
        response.write_int(3)
        response.write_bool(True)
        response.write_string("1448526834")
        response.write_bool(True)
        response.write_bool(False)
        session.send(response)

        response = Response(2925)
        response.write_int(1)
        response.write_int(0)
        response.write_int(0)
        session.send(response)