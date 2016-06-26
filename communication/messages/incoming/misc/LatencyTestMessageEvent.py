"""
Check release of SWF version
Author: Alex (TheAmazingAussie)
"""


class LatencyTestMessageEvent:
    def handle(self, session, message):
        session.connection.packet_check()