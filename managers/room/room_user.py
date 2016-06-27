"""
Room user
Author: Alex (TheAmazingAussie)
"""

class RoomUser:
    def __init__(self, session):
        self.dispose()
        self.entity = session

    def dispose(self):
        self.virtual_id = 0
        self.last_chat_id = 0
        self.dance_id = 0
        self.position = None
        self.goal = None
        self.rotation = 0
        self.head_rotation = 0
        self.statuses = {}
        self.path = []
        self.room = None
        self.is_walking = False
        self.needs_update = False
        self.is_loading_room = False
        self.in_room = False
        self.entity = None
        self.chat_flood_timer = 0
        self.chat_count = 0
