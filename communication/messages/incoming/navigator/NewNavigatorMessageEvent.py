"""
Check release of SWF version
Author: Alex (TheAmazingAussie)
"""

import util.logging as log


class NewNavigatorMessageEvent:
    def handle(self, session, message):
        """
        Enable navigator when requested
        :param session: the clients who requests NewNavigatorMessageEvent handler
        :param message: the incoming message
        """

        
