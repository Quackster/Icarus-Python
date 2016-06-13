from communication.packets.LOGIN import *


class Messages:
    def __init__(self):
        self.packets = []
        self.packets.append(LOGIN())

    def incoming_message(self, connection, header, message):

        for message in self.packets:
            if message.__class__.__name__ == header:
                message.handle(connection, message)