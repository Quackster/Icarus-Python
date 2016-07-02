"""
Room mapping
Author: Alex (TheAmazingAussie)
"""
import managers.room.model.room_model as model

class RoomMapping:
    def __init__(self, room):
        self.room = room
        self.collision_map = None

    def regenerate_collision_map(self):
        """
        Create collision map used for pathfinding
        :return:
        """

        # Create fresh collision map array
        self.collision_map = self.room.get_model().get_2d_array()

        # Details about whether or not default model squares are blocked
        squares = self.room.get_model().squares

        # Fill blocking details
        for y in range(0, self.room.get_model().map_size_y):
            for x in range (0, self.room.get_model().map_size_x):
                self.collision_map[x][y] = squares[x][y]

    def update_map(self, x, y, is_blocked):
        """
        Update map with details if certain squares are blocked
        :param x: x coordinate
        :param y: y coordinate
        :param is_blocked: true/false to block tile
        :return:
        """
        if is_blocked:
            self.collision_map[x][y] = model.CLOSED
        else:
            self.collision_map[x][y] = model.OPEN

    def is_closed(self, x, y):
        """
        Returns whether or not a coordinate in the room is closed
        :param x: x coordinate
        :param y: y coordinate
        :return:
        """
        return self.collision_map[x][y] == model.CLOSED

    def is_open(self, x, y):
        """
        Returns whether or not a coordinate in the room is open
        :param x: x coordinate
        :param y: y coordinate
        :return:
        """
        return self.collision_map[x][y] == model.OPEN

    def dispose(self):
        """
        Dispose all collision map properties
        :return:
        """
        del self.collision_map