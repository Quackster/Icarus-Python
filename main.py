"""
Main file to call program
Author: Alex (TheAmazingAussie)
"""

import game
import util.logging as log
from network.server import Server
from database.database_connect import DatabaseConnection
import database.database_access as dao


# Main program below this line
log.line("################")
log.line("##   Icarus   ##")
log.line("################")
log.line()
log.line("Written by Quackster/TheAmazingAussie")
log.line()
log.info("Test Habbo Hotel python server.")
log.info()
log.info("Testing MySQL connnection")
db_error = False

try:
    DatabaseConnection().create_connection()
except Exception as e:
    db_error = True
    log.error("Could not connect to database")
    log.error(str(e))
    exit()

if not db_error:
    log.info("MySQL connection was successful")


log.info()
log.info("Loading data access objects")
dao.init_dao()

log.info()
log.info("Loading game instance")
game.init_game()

log.info()
log.info("Starting network")

port = 3242;
ip = "localhost"

try:
    game.server = Server(ip, port)
    log.info("Listening on port " + str(port))
except Exception as e:
    log.error("Could not bind to port: " + str(e))
