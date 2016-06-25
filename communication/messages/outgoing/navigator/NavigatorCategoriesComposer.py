import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class NavigatorCategoriesComposer:
    def __init__(self, categories):

        self.response = Response(outgoing.NavigatorCategories)
        self.response.write_int(4 + len(categories))

        for category in categories:
            self.response.write_string("category__" + category)


        self.response.write_string("recommended")
        self.response.write_string("new_ads")
        self.response.write_string("staffpicks")
        self.response.write_string("official")
