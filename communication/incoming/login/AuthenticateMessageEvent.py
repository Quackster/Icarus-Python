import util.logging as log
from communication.messages.response import *


class AuthenticateMessageEvent:
    def handle(self, session, message):
        """
        Handle sso request
        :param session: the session who requests AuthenticateMessageEvent handler
        :param message: the incoming message with login details
        """

        log.session("SSO ticket: " + message.read_string())

        response = Response(1552)
        session.send(response)
        log.write_to_file("test", response.get_buffer().decode("ascii"))