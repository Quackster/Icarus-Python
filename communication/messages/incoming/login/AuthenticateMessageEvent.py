"""
Authenticate user class using received SSO ticket
Author: Alex (TheAmazingAussie)
"""

import database.database_access as dao
import util.logging as log

from communication.messages.outgoing.login.UniqueMachineIDMessageComposer import *
from communication.messages.outgoing.login.AuthenticationOKMessageComposer import *
from communication.messages.outgoing.login.HomeRoomMessageComposer import *
from communication.messages.outgoing.login.LandingWidgetMessageComposer import *
from communication.messages.outgoing.user.MOTDMessageComposer import *


class AuthenticateMessageEvent:
    def handle(self, session, message):
        """
        Handle sso request
        :param session: the clients who requests AuthenticateMessageEvent handler
        :param message: the incoming message with login details
        """
        sso_ticket = message.read_string()

        if not dao.user.authenticate(session, sso_ticket):
            session.close()
            return

        session.send(AuthenticationOKMessageComposer())
        session.send(UniqueMachineIDMessageComposer(session.details.machine_id))
        session.send(HomeRoomMessageComposer(0, False))
        session.send(LandingWidgetMessageComposer())

        # MOTD
        session.send(MOTDMessageComposer("Hello, welcome to Icarus Server\n\nThe only Habbo hotel private server written in Python!"))


        # Load user rooms
        dao.room_dao.get_player_rooms(session.details, True)