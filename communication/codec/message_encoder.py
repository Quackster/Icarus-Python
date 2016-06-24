"""
Class for decoding messages which are received
Author: Alex (TheAmazingAussie)
"""

import game
from communication.messages.request import *


def encode(response):
    """
    Parse incoming data from client
    :param session: the session who is currently connected
    :param response: the message to parse
    """

    if type(response) is str:
        return response.encode()
    else:
        return response.get_buffer()
