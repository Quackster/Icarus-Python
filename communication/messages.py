from communication.packets.LOGIN import *


class Messages:
    def __init__(self):
        self.packets = []
        self.packets.append(LOGIN())

    def incoming_message(self, connection, header, message):
        """
        Locate the incoming message and handle it
        :param connection: the session connected
        :param header: the class name requested
        :param message: the rest of the message
        :return:
        """
        for message in self.packets:
            if message.__class__.__name__ == header:
                message.handle(connection, message)