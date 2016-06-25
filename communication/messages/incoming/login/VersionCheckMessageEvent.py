"""
Check release of SWF version
Author: Alex (TheAmazingAussie)
"""

import util.logging as log


class VersionCheckMessageEvent:
    def handle(self, session, message):
        """
        Handle login request
        :param session: the session who requests CheckReleaseMessageEvent handler
        :param message: the incoming message with login details
        """

        swf_revision = message.read_string()
        log.session("Version check, swf revision: " + swf_revision)
