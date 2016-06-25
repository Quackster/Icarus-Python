class user_dao:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def authenticate(self, session, sso_ticket):
        """
        Verifies if a connecting client has a valid SSO ticket when logging into the server
        :param sso_ticket: the ticket which logs in the user from the client
        :return: Boolean if user is successfully validated
        """
        db_con = self.database_connection.create_connection()
        db_cur = db_con.cursor()
        db_cur.execute("SELECT id, username, rank, sso_ticket, motto, figure, credits FROM users WHERE sso_ticket = %s LIMIT 1", (sso_ticket))

        has_row = db_cur.rowcount > 0

        db_con.close()
        db_cur.close()

        return has_row