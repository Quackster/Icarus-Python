import communication.headers.outgoing as outgoing
from communication.data_streams.response import Response


class FlatCategoriesMessageComposer:
    def __init__(self, categories):

        self.response = Response(outgoing.FlatCategoriesMessageComposer)
        self.response.write_int(len(categories))

        index = 0

        for category in categories:
            self.response.write_int(index)
            self.response.write_string(category)
            self.response.write_bool(True)
            self.response.write_bool(False)
            self.response.write_string("NONE")
            self.response.write_string("")
            self.response.write_bool(False)
            index += 1