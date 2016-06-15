class LOGIN:
    def handle(self, session, message):
        """
        Handle login request
        :param session: the session who requests LOGIN handler
        :param message: the incoming message with login details
        :return:
        """
        print ("USEROBJECT" + chr(13) + session.details.get_user_object())