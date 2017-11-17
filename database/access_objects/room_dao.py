"""
Room data access object
Author: Alex (TheAmazingAussie)
"""
import game
from managers.room.room import Room
from managers.room.model.room_model import RoomModel


class RoomDao:
    def __init__(self, database_connection):
        self.database_connection = database_connection
        self.room_models = {}

    def get_models(self):
        db_con = self.database_connection.create_connection()
        db_cur = db_con.cursor()
        db_cur.execute("SELECT id, heightmap, door_x, door_y, door_z, door_dir FROM room_models")

        for row in db_cur:
            model = RoomModel(row[0], row[1], int(row[2]), int(row[3]), int(row[4]), row[5])
            self.room_models[model.name] = model

        db_con.close()
        db_cur.close()

        return self.room_models

    def get_player_rooms(self, details, store_in_memory):
        """
        Returns tabs specified by child_id
        :param child_id: the child id, if -1 will show all tabs with no parents
        """

        db_con = self.database_connection.create_connection()
        db_cur = db_con.cursor()

        db_cur.execute("SELECT * FROM rooms WHERE owner_id = %s", (details.id))

        rooms = []

        for row in db_cur:
            room = Room()
            self.fill_data(room, row)

            if store_in_memory:
                game.room_manager.add_room(room)

        db_con.close()
        db_cur.close()

        return rooms

    def get_room(self, room_id, store_in_memory):
        """
        Returns tabs specified by child_id
        :param child_id: the child id, if -1 will show all tabs with no parents
        """

        if room_id in game.room_manager.rooms:
            return game.room_manager.rooms[room_id]

        db_con = self.database_connection.create_connection()
        db_cur = db_con.cursor()
        db_cur.execute("SELECT * FROM rooms WHERE id = %s LIMIT 1", (room_id))

        room = None

        for row in db_cur:
            room = Room()
            self.fill_data(room, row)

            if store_in_memory:
                game.room_manager.add_room(room)

        db_con.close()
        db_cur.close()

        return room

    def fill_data(self, room, row):
        """
        Fill instance with given row data
        :param room: the data instance to fill
        :param row: the row fected with MySQL
        :return:
        """
        room.data.id = row[0]
        room.data.name = row[1]
        room.data.type = row[2]
        room.data.owner_id = row[4]
        room.data.group_id = row[5]
        room.data.description = row[7]
        room.data.password = row[8]
        room.data.users_now = row[9]
        room.data.users_max = row[10]
        room.data.model = row[11]
        room.data.wall = row[12]
        room.data.floor = row[13]
        room.data.landscape = row[14]
        room.data.tags = row[15].split(",")
        room.data.trade_state = row[16]

        _state = row[17]

        if _state == "OPEN":
            room.data.state == 0

        if _state == "INVISIBLE":
            room.data.state == 3

        if _state == "DOORBELL":
            room.data.state == 1

        if _state == "PASSWORD":
            room.data.state == 2

        room.data.score = row[18]
        room.data.category = row[19]
        room.data.allow_pets = row[20] == 1
        room.data.allow_pets_eat = row[21] == 1
        room.data.allow_walkthrough = row[22] == 1
