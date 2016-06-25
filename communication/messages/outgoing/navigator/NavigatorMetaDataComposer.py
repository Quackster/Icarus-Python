import communication.headers.outgoing as outgoing
import game
from communication.data_streams.response import Response


class NavigatorMetaDataComposer:
    def __init__(self):
        self.response = Response(outgoing.NavigatorMetaDataComposer)
        self.response.write_int(len(game.navigator_manager.get_parent_tabs()))

        for tab in game.navigator_manager.get_parent_tabs():
            self.response.write_string(tab.tab_name)
            self.response.write_int(0)
