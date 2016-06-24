
"""
Class for translating raw bytes to readable numbers
Author: TheAmazingAussie/Alex
"""

import struct


class Request:
    def __init__(self, stream):
        self.stream = stream
        self.index = 0

    def read_short(self):
        """
        Read 16 bits as a integer
        :return: integer
        """
        num = struct.unpack_from(">h", self.stream, self.index)[0]
        self.index += 2
        return int(num)

    def read_int(self):
        """
        Read 32 bits as integer
        :return: integer
        """
        num = struct.unpack_from(">i", self.stream, self.index)[0]
        self.index += 4
        return int(num)

    def read_string(self):
        """
        Read string encoded in UTF-8 from packet with int16 prefix
        :return: string
        """
        str_length = self.read_short()
        str = self.get()[self.index:self.index + str_length]
        self.index += str_length
        return str

    def get(self):
        """
        Get received packet as string in ISO-8859-1 encoding
        :return: packet as string
        """
        return self.stream.decode("ISO-8859-1")