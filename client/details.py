class Details:

    def __init__(self):
        self.username = ""
        self.password = ""
        self.email = ""
        self.pants = ""
        self.shirt = ""
        self.head = ""
        self.age = ""
        self.mission = ""

    def get_user_object(self):
        return self.username + " " + self.password + " " + self.email + " " + self.pants + "," + self.shirt + "," + self.head + " " + "noidea x " + "Male" + " yes " + self.age + " " + self.mission;