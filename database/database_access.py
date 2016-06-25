"""
Data access object class
author: TheAmazingAussie (Alex)
"""

from database.database_connect import DatabaseConnection
from database.dao.user_dao import UserDao

# Database connection class
__dbconnect = DatabaseConnection()

# Data access objects
user = UserDao(__dbconnect)