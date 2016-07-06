import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class FlatCategoriesMessageComposer:
    def __init__(self, categories, rank):

        self.response = Response(outgoing.FlatCategoriesMessageComposer)
        self.response.write_int(len(categories))

        for category in categories:
            self.response.write_int(category.id)
            self.response.write_string(category.name)
            self.response.write_bool(category.min_rank <= rank)
            self.response.write_bool(False)
            self.response.write_string("NONE")
            self.response.write_string("")
            self.response.write_bool(False)