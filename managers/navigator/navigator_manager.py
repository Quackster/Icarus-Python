"""
Navigator Manager
Author: Alex (TheAmazingAussie)
"""

import database.database_access as dao


class NavigatorManager:
    def __init__(self):
        self.tabs = dao.navigator.get_tabs(-1)

    def get_tab(self, name):
        """
        Get tab by name, includes parent and child tabs
        :param name: the name of the tab
        :return: tab instance
        """
        for tab in self.tabs:
            if tab.tab_name == name:
                return tab

    def get_parent_tabs(self):
        """
        Return all child tabs
        :return: list of child tab instances
        """
        tabs = []
        for tab in self.tabs:
            if tab.child_id == -1:
                tabs.append(tab)

        return tabs


