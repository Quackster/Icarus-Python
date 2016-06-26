import game
from managers.room.room import Room


class RoomDao:
    def __init__(self, database_connection):
        self.database_connection = database_connection

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
        room.data.owner_id = row[3]
        room.data.group_id = row[4]
        room.data.description = row[5]
        room.data.password = row[6]
        room.data.users_now = row[7]
        room.data.users_max = row[8]
        room.data.model = row[9]
        room.data.wall = row[10]
        room.data.floor = row[11]
        room.data.landscape = row[12]
        room.data.tags = row[13].split(",")
        room.data.trade_state = row[14]
        room.data.state = row[15]
        room.data.category = row[16]