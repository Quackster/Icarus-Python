"""
Navigator Manager
Author: Alex (TheAmazingAussie)
"""

import database.database_access as dao

class NavigatorManager:
    def __init__(self):
        self.tabs = dao.navigator.get_tabs(-1)
