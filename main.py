import network.server as server
from communication.messages import *

import util.logging as log
import variables

log.info("Mobiles disco test network.")
log.info("Loading packet handler")
variables.messages = Messages()

log.info("Starting network")

variables.port = 91;
variables.ip = "localhost"

try:
    variables.async_server = server.Server(variables.ip, variables.port)
    log.info("Listening on port " + str(variables.port))
except Exception as e:
    log.error("Could not bind to port: " + str(e))
