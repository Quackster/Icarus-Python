import network.server as server
from communication.messages import *

import util.logging as log
import game

log.info("Mobiles disco test network.")
log.info("Loading packet handler")
game.messages = Messages()

log.info("Starting network")

game.port = 91;
game.ip = "localhost"

try:
    game.async_server = server.Server(game.ip, game.port)
    log.info("Listening on port " + str(game.port))
except Exception as e:
    log.error("Could not bind to port: " + str(e))
