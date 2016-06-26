"""
Check release of SWF version
Author: Alex (TheAmazingAussie)
"""


class EventLogMessageEvent:
    def handle(self, session, message):
        session.connection.packet_check()