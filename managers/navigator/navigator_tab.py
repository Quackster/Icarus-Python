"""
Navigator tab instance
author: TheAmazingAussie (Alex)
"""
import game


class NavigatorTab:
    def __init__(self):
        self.id = 0
        self.child_id = 0
        self.tab_name = ""
        self.title = ""
        self.button_type = ""
        self.closed = False
        self.thumbnail = False
        self.populator = None

    def get_child_tabs(self):
        tabs = []
        for tab in game.navigator_manager.tabs:
            if tab.child_id == self.id:
                tabs.append(tab)

        return tabs