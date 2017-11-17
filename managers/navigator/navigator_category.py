"""
Navigator category instance
author: TheAmazingAussie (Alex)
"""
import game


class NavigatorCategory:

    def __init__(self, id, name, min_rank):
        self.id = id
        self.name = name
        self.min_rank = min_rank
        self.navigator_visible = True

