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
        self.button_type = 0
        self.closed = False
        self.thumbnail = False
        self.show_categories = False
        self.populator = None

    def get_child_tabs(self):
        """
        Get all child tabs under this tab
        :return: the list of tabs
        """
        return [tab for tab in game.navigator_manager.tabs if tab.child_id == self.id]