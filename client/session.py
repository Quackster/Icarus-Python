import variables


class Session:
    def __init__(self, socket):
        self.socket = socket

    def close(self):
        print ("closed br00")
        variables.connections.remove(self)

