"""
Data access object class
author: TheAmazingAussie (Alex)
"""

import util.logging as log
from database.database_connect import DatabaseConnection
from database.dao.user_dao import UserDao
from database.dao.navigator_dao import NavigatorDao
from database.dao.room_dao import RoomDao

"""
:type user: UserDao
:type navigator: NavigatorDao
"""
user = None
navigator = None
room = None

#try:
# Database connection class
__dbconnect = DatabaseConnection()

# Data access objects
user = UserDao(__dbconnect)
navigator = NavigatorDao(__dbconnect)
room = RoomDao(__dbconnect)
#except Exception as e:
#    log.error("Error caught (" + __file__  + "): " + str(e))