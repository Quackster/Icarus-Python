"""
Main file to call program
Author: Alex (TheAmazingAussie)
"""

import network.server as server
from communication.message_handler import *

import util.logging as log
import game

log.line("###############")
log.line("## pyHabbo ##")
log.line("###############")
log.line()
log.line("Written by Quackster/TheAmazingAussie")
log.line()
log.info("Test Habbo Hotel python server.")
log.info("Loading packet handler")
game.message_handler = MessageHandler()

log.info("Starting network")

port = 3242;
ip = "localhost"

#try:
game.async_server = server.Server(ip, port)
log.info("Listening on port " + str(port))
#except Exception as e:
    #log.error("Could not bind to port: " + str(e))
