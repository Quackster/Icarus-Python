"""
Main file to call program
Author: Alex (TheAmazingAussie)
"""

import util.logging as log
import network.server as server
import game
from network.server import *
from communication.message_handler import *

# Main program below this line
log.line("###############")
log.line("##  pyHabbo  ##")
log.line("###############")
log.line()
log.line("Written by Quackster/TheAmazingAussie")
log.line()
log.info("Test Habbo Hotel python server.")


log.info("Starting network")

port = 3242;
ip = "localhost"

try:
    game.server = Server(ip, port)
    log.info("Listening on port " + str(port))
except Exception as e:
    log.error("Could not bind to port: " + str(e))

log.info("Loading packet handler")
game.message_handler = MessageHandler()