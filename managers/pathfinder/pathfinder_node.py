"""
Pathfinder node class
"""
import sys
from managers.pathfinder.point import Point

class PathfinderNode:
    def __init__(self, position):

        self.position = Point(0, 0, 0)

        if position is not None:
            self.position = position

        self.next_node = None
        self.cost = sys.maxsize
        self.in_open = False
        self.in_close = False