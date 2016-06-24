import util.logging as log
from communication.messages.response import *


class VersionCheckMessageEvent:
    def handle(self, session, message):
        """
        Handle login request
        :param session: the session who requests CheckReleaseMessageEvent handler
        :param message: the incoming message with login details
        """

        log.session("Version check, swf revision: " + message.read_string())
