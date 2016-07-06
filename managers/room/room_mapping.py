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

    def is_valid_step(self, current, tmp, final_move):
        """
        Check if the attempted space is a valid step to walk in
        :param room: the room of the pathfinder calculation
        :param current: the current coordinate
        :param tmp: the coordinate to check from around the current coord
        :param final_move: if this is the last coordinate check
        :return:
        """
        try:

            # Stop user walking diagonally through solid objects
            if current.x != tmp.x and current.y != tmp.y:

                diagonal1 = self.is_closed(tmp.x, current.y)
                diagonal2 = self.is_closed(current.x, tmp.y)

                if diagonal1 or diagonal2:
                    return False

            return self.is_open(tmp.x, tmp.y)

        except Exception as e:
            return False

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
        try:
            del self.collision_map
        except Exception as e:
            return