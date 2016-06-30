"""
Packet checking class
Author: Alex (TheAmazingAussie)
"""


class EventLogMessageEvent:
    def handle(self, session, message):
        session.connection.packet_check()