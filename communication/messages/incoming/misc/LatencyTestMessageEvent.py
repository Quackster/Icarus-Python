"""
Packet checking class
Author: Alex (TheAmazingAussie)
"""


class LatencyTestMessageEvent:
    def handle(self, session, message):
        session.connection.packet_check()