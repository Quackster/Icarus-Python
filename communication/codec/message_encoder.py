"""
Class for encoding messages which are sent
Author: Alex (TheAmazingAussie)
"""

from communication.data_streams.response import Response


def encode(response):
    """
    Parse incoming data from client
    :param clients: the clients who is currently connected
    :param response: the message to parse
    """

    if type(response) is str:
        return response.encode()
    elif type(response) is Response:
        return response.get_buffer()
    else:
        return response.response.get_buffer()
