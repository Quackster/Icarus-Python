"""
Data access object class
author: TheAmazingAussie (Alex)
"""

import util.logging as log
from database.database_connect import DatabaseConnection
from database.dao.user_dao import UserDao

try:
    # Database connection class
    __dbconnect = DatabaseConnection()

    # Data access objects
    user = UserDao(__dbconnect)
except Exception as e:
    log.error("Error caught (" + __file__  + "): " + str(e))