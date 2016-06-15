import network.server as server
from communication.messages import *

import util.logging as log
import game

log.line("###############")
log.line("## pyMobiles ##")
log.line("###############")
log.line()
log.line("Written by Quackster/TheAmazingAussie")
log.line()
log.info("Mobiles disco test server.")
log.info("Loading packet handler")
game.messages = Messages()

log.info("Starting network")

port = 91;
ip = "localhost"

try:
    game.async_server = server.Server(ip, port)
    log.info("Listening on port " + str(port))
except Exception as e:
    log.error("Could not bind to port: " + str(e))
