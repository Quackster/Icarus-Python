"""
Room manager
Author: Alex (TheAmazingAussie)
"""


class RoomManager:
    def __init__(self):
        self.rooms = {}

    def load_manager(self):
        #TODO: Load public rooms
        return

    def add_room(self, room):
        """
        Add room to collection of rooms, will not add if there's an existing room
        :param room: the room instance
        :return: None
        """
        if room.data.id not in self.rooms:
            self.rooms[room.data.id] = room

    def get_player_rooms(self, user_id):
        """
        Return all rooms owned by player
        :param user_id: the owner id of the rooms
        :return:
        """
        _rooms = []

        for room_id, room in self.rooms.items():

            if room.data.owner_id == user_id:
                _rooms.append(room)

        return _rooms