"""
Authenticate user class using received SSO ticket
Author: Alex (TheAmazingAussie)
"""


class UniqueIDMessageEvent:
    def handle(self, session, message):
        """
        Handle sso request
        :param session: the clients who requests AuthenticateMessageEvent handler
        :param message: the incoming message with login details
        """
        message.read_string()
        unique_machine_id = message.read_string()
        session.details.machine_id = unique_machine_id
