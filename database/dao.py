"""
Data access object class
author: TheAmazingAussie (Alex)
"""

from database.dbconnect import DatabaseConnection
from database.user.user_dao import *

# Database connection class
__dbconnect = DatabaseConnection()

# Data access objects
user = user_dao(__dbconnect)