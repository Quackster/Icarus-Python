"""
Display information for user event
Author: Alex (TheAmazingAussie)
"""

from communication.messages.outgoing.user.SendPerkAllowancesMessageComposer import SendPerkAllowancesMessageComposer
from communication.messages.outgoing.user.UserObjectMessageComposer import UserObjectMessageComposer


class InfoRetrieveMessageEvent:
    def handle(self, session, message):
        """
        Send user info
        :param session: the clients who requests InfoRetrieveMessageEvent handler
        :param message: the incoming message
        """

        session.send(SendPerkAllowancesMessageComposer())
        session.send(UserObjectMessageComposer(session.details))