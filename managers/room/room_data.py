"""
Room data
Author: Alex (TheAmazingAussie)
"""


class RoomData:
    def __init__(self):
        self.id = -1
        self.type = ""
        self.owner_id = -1
        self.owner_name = "Alex"
        self.name = ""
        self.state = ""
        self.password = ""
        self.thumbnail = ""
        self.users_now = 0
        self.users_max = 0
        self.description = ""
        self.trade_state = 0
        self.score = 0
        self.category = 0
        self.group_id = 0
        self.model = ""
        self.wall = ""
        self.floor = ""
        self.landscape = ""
        self.allow_pets = True
        self.allow_pets_eat = False
        self.allow_walkthrough = False
        self.hide_wall = False
        self.wall_thickness = 0
        self.floor_thickness = 0
        self.wall_height = -1
        self.tags = []
        self.chat_type = 0
        self.chat_balloon = 0
        self.chat_speed = 0
        self.chat_max_distance = 0
        self.chat_flood_protection = 0
        self.who_can_mute = 0
        self.who_can_kick = 0
        self.who_can_ban = 0

    def serialise(self, response, enter_room):
        
        response.write_int(self.id)
        response.write_string(self.name)
        response.write_int(self.owner_id)
        response.write_string(self.owner_name)
        response.write_int(self.state)
        response.write_int(self.users_now)
        response.write_int(self.users_max)
        response.write_string(self.description)
        response.write_int(self.trade_state)
        response.write_int(self.score)
        response.write_int(0)
        response.write_int(self.category)
        response.write_int(len(self.tags))

        for tag in self.tags:
            response.write_string(tag)
        
        enum_type = 0

        if enter_room:
            enum_type = 32
        
        ## if has event
        ##enumType += 4;

        if self.thumbnail is not None:
            if len(self.thumbnail) > 0:
                enum_type += 1

        if self.type == 0: # 0 being private
            enum_type += 8

        if self.allow_pets:
            enum_type += 16

        response.write_int(enum_type)
        
        if self.thumbnail is not None:
            if len(self.thumbnail) > 0:
                response.write_string(self.thumbnail)
