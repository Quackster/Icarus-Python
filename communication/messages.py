from communication.packets.LOGIN import *


class Messages:
    def __init__(self):
        self.packets = []
        self.packets.append(LOGIN())

    def incoming_message(self, connection, header, message):

        for message in self.packets:
            if message.header == header:
                message.handle(connection, message)