"""
Check release of SWF version
Author: Alex (TheAmazingAussie)
"""

from communication.messages.outgoing.user.CreditsBalanceMessageComposer import CreditsBalanceMessageComposer


class CurrencyBalanceMessageEvent:
    def handle(self, session, message):
        """
        Send current currency balance
        :param session: the clients who requests CurrencyBalanceMessageEvent handler
        :param message: the incoming message with login details
        """

        session.send(CreditsBalanceMessageComposer(session.details.credits))