class UserDao:
    def __init__(self, database_connection):
        self.database_connection = database_connection

    def authenticate(self, session, sso_ticket):
        """
        Verifies if a connecting client has a valid SSO ticket when logging into the server
        :param sso_ticket: the ticket which logs in the dao from the client
        :param session: the session connected with the sso ticket
        :return: Boolean if dao is successfully validated
        """
        db_con = self.database_connection.create_connection()
        db_cur = db_con.cursor()
        db_cur.execute("SELECT id, username, rank, motto, figure, credits FROM users WHERE sso_ticket = %s LIMIT 1", (sso_ticket))

        has_row = db_cur.rowcount > 0

        for row in db_cur:
            session.details.id = row[0]
            session.details.username = row[1]
            session.details.rank = row[2]
            session.details.motto = row[3]
            session.details.figure = row[4]
            session.details.credits = 5000

        db_con.close()
        db_cur.close()

        return has_row