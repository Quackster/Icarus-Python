class LOGIN:
    def handle(self, session, message):
        """
        Handle login request
        :param session: the session who requests LOGIN handler
        :param message: the incoming message with login details
        :return:
        """
        print ("Login request")