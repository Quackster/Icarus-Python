import game
import communication.headers.outgoing as outgoing

from communication.data_streams.response import Response


class SearchResultSetComposer:
    def __init__(self, session, tab, search_query):

        categories = game.navigator_manager.get_navigator_categories()

        self.response = Response(outgoing.SearchResultSetComposer)
        self.response.write_string(tab.tab_name)
        self.response.write_string(search_query)

        # If empty search query
        if len(search_query) == 0:

            tabs = []
            room_limit = True

            if tab.child_id != -1:
                tabs.append(tab)
                room_limit = False
            else:
                tabs += (tab.get_child_tabs())

            if tab.show_categories:
                self.response.write_int(len(tabs) + len(categories))
            else:
                self.response.write_int(len(tabs))

            for navigator_tab in tabs:
                self.response.write_string(navigator_tab.tab_name)
                self.response.write_string(navigator_tab.title)

                if room_limit:
                    self.response.write_int(navigator_tab.button_type)
                    self.response.write_bool(navigator_tab.thumbnail)
                else:
                    self.response.write_int(2)
                    self.response.write_bool(False)

                self.response.write_bool_int(navigator_tab.thumbnail)

                _rooms = navigator_tab.populator.generate_listing(room_limit, session)

                self.response.write_int(len(_rooms)) # room_dao count

                for room in _rooms:
                    room.data.serialise(self.response, False)

            if tab.show_categories:
                for category in categories:
                    self.response.write_string(category.name.lower().replace(" ", "_").replace(",", "").replace("&", "").replace("__", "_"))

                    print (category.name.lower().replace(" ", "_").replace(",", "").replace("&", "").replace("__", "_") + "=" + category.name)

                    self.response.write_string("")
                    self.response.write_int(2)
                    self.response.write_bool(False)
                    self.response.write_int(0)

                    _rooms = []
                    self.response.write_int(len(_rooms)) # room_dao count

                    for room in _rooms:
                        room.data.serialise(self.response, False)



        else:
            self.response.write_int(0)