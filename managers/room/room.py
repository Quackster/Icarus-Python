"""
Room instance
Author: Alex (TheAmazingAussie)
"""
from managers.room.room_data import RoomData


class Room:
    def __init__(self):
        self.data = RoomData()
        self.entities = []

    def has_rights(self, user_id, only_owner_check):
        return False