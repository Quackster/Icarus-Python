import network.server as server
from communication.messages import *

import sys
import util.logging as log
import variables

log.info("Mobiles disco test network.")
log.info("Loading packet handler")
variables.messages = Messages()

log.info("Starting network")

variables.port = 91;
variables.ip = "localhost"

try:
    async_server = server.Server(variables.ip, variables.port)
    async_server.listener.loop()
except:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    log.error(str(exc_value))