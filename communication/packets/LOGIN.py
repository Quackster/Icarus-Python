class LOGIN:

    def __init__(self):
        self.header = "LOGIN"

    def handle(self, session, message):

        print ("Login request", self.header)
