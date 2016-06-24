"""
Response class for sending packets back to client
Author: Alex (TheAmazingAussie)
"""

import struct


class Response:

    def __init__(self, header):
        """
        Create response instance with given header
        :param header: Integer header containing 32 bits
        """
        self.header = header
        self.buffer = bytearray()
        self.index = 0

        self.write_short(header)

    def write_short(self, number):
        """
        Write short with 16 bits (number)
        :param number: the number to write
        :return:
        """
        self.buffer.extend(struct.pack(">h", number))
        self.index += 2

    def write_int(self, number):
        """
        Write integer with 32 bits
        :param number: the number to write
        """
        self.buffer.extend(struct.pack(">i", number))
        self.index += 4

    def write_string(self, string):
        """
        Append string in UTF-8 encoding, prefixed in int16/short with the length of string
        :param string: The string to write
        """
        str_len = len(string)

        self.write_short(str_len)
        self.buffer.extend(bytes(string, "utf8"))

        self.index += str_len

    def write_bool_int(self, bool):
        """
        Write a 0 or 1 in int32 when a boolean is given
        :param bool: true or false parameter
        """
        if bool:
            self.write_int(1)
        else:
            self.write_int(0)

    def write_bool(self, bool):
        """
        Write a 0 or 1 in single bit when a boolean is given
        :param bool: true or false parameter
        """
        if bool:
            self.buffer.extend(1)
        else:
            self.buffer.extend(0)

        self.index += 1

    def get_buffer(self):
        """
        Get raw byte array, prefixed with int32 number with length of packet
        :return: byte array
        """
        new_buffer = bytearray()
        new_buffer.extend(struct.pack(">i", len(self.buffer)))
        new_buffer.extend(self.buffer)
        return new_buffer