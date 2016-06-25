"""
Authenticate user class using received SSO ticket
Author: Alex (TheAmazingAussie)
"""

import database.database_access as dao
import util.logging as log

#Packets
from communication.messages.outgoing.login.UniqueMachineIDMessageComposer import *
from communication.messages.outgoing.login.AuthenticationOKMessageComposer import *
from communication.messages.outgoing.login.HomeRoomMessageComposer import *
from communication.messages.outgoing.login.LandingWidgetMessageComposer import *


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
            print ("Invalid sso ticket, kicking dao")
            session.close()
            return

        session.send(AuthenticationOKMessageComposer())
        session.send(UniqueMachineIDMessageComposer(session.details.machine_id))
        session.send(HomeRoomMessageComposer(0, False))
        session.send(LandingWidgetMessageComposer())