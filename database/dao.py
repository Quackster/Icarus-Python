"""
Data access object class
author: TheAmazingAussie (Alex)
"""

from database.dbconnect import db_connection
from database.user.user_dao import *

# Database connection class
__dbconnect = db_connection()

# Data access objects
__user_dao = user_dao(__dbconnect)

# Access the DAO instances
def get_user_dao():
    return __user_dao
