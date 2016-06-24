"""
Class for encoding messages which are sent
Author: Alex (TheAmazingAussie)
"""

from communication.messages.response import Response


def encode(response):
    """
    Parse incoming data from client
    :param session: the session who is currently connected
    :param response: the message to parse
    """

    if type(response) is str:
        return response.encode()

    if type(response) is Response:
        return response.get_buffer()
