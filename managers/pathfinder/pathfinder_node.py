"""
Pathfinder node class
"""
import sys
from managers.pathfinder.point import Point


class PathfinderNode:
    def __init__(self, position):
        self.next_node = None
        self.in_open = False
        self.in_close = False
        self.position = position
        self.cost = sys.maxsize