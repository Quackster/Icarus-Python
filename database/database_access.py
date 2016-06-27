"""
Data access object class
author: TheAmazingAussie (Alex)
"""

import util.logging as log
from database.database_connect import DatabaseConnection
from database.access_objects.user_dao import UserDao
from database.access_objects.navigator_dao import NavigatorDao
from database.access_objects.room_dao import RoomDao

user = None
navigator = None
room_dao = None

try:
    # Database connection class
    db_connect = DatabaseConnection()

    # Data access objects
    user = UserDao(db_connect)
    navigator = NavigatorDao(db_connect)
    room_dao = RoomDao(db_connect)

except Exception as e:
    log.error("Error caught (" + __file__  + "): " + str(e))


def init_dao():
    """
    Query database after DAO class has initialised
    :return:
    """
    room_dao.get_models()