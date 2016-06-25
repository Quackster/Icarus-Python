"""
Session (user) details
Author: Alex (TheAmazingAussie)
"""


class Details:

    def __init__(self):
        self.id = -1;
        self.username = "Alex";
        self.motto = "";
        self.figure = "";
        self.rank = 1;
        self.credits = 0;
        self.machine_id = ""
        self.authenticated = False

    def fill_details(self, id, username, motto, figure, rank, credits):
        self.id = id
        self.username = username
        self.motto = motto
        self.figure = figure
        self.rank = rank
        self.credits = credits

    def get_user_object(self):
        return ""