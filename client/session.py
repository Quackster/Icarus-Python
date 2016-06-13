import variables


class Session:
    def __init__(self, socket):
        self.socket = socket

    def close(self):
        """
        Force lose socket on demand
        :return:
        """
        variables.connections.remove(self)
        self.socket.close()

        print ("SOCKET CLOSED")

