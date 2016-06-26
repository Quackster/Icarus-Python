"""
Class for encoding messages which are sent
Author: Alex (TheAmazingAussie)
"""

from communication.data_streams.response import Response


def encode(message):
    """
    Return outcoming data from client
    :param response: the message to parse for client
    """

    # Convert string to bytes
    if type(message) is str:
        return message.encode()

    # Build message in bytes for client from response class
    elif type(message) is Response:
        return message.get_buffer()

    # Assume this is a composer class
    # Build message in bytes for clients from composer
    else:
        return message.response.get_buffer()
