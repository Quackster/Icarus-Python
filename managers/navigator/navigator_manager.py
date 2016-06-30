"""
Navigator Manager
Author: Alex (TheAmazingAussie)
"""

import database.database_access as dao
from managers.navigator.populators.default_room_populator import DefaultRoomPopulator
from managers.navigator.populators.my_room_populator import MyRoomPopulator
from managers.navigator.populators.popular_room_populator import PopularRoomPopulator


class NavigatorManager:

    def __init__(self):
        self.populators = {
            "DefaultRoomPopulator": DefaultRoomPopulator(),
            "MyRoomPopulator": MyRoomPopulator(),
            "PopularRoomPopulator": PopularRoomPopulator()
        }

    def load_manager(self):
        self.tabs = dao.navigator.get_tabs(-1)

    def get_tab(self, name):
        """
        Get tab by name, includes parent and child tabs
        :param name: the name of the tab
        :return: tab instance
        """
        _gathered_tabs = [tab for tab in self.tabs if tab.tab_name == name]
        return _gathered_tabs[0] # Select first tab

    def get_parent_tabs(self):
        """
        Return all child tabs
        :return: list of child tab instances
        """
        return [tab for tab in self.tabs if tab.child_id == -1]

    def get_populator(self, name):
        """
        Adds a room_dao listing populator by name, will return default populator if nothing was specified
        :param name: class name of populator
        """
        if name in self.populators:
            return self.populators[name]
        else:
            return self.populators["DefaultRoomPopulator"]



