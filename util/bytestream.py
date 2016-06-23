
"""
Class for translating raw bytes to readable numbers
Author: TheAmazingAussie/Alex
"""

import struct

class ByteStream:
    def __init__(self, stream):
        self.stream = stream
        self.index = 0

    def read_short(self):
        num = struct.unpack_from(">h", self.stream, self.index)[0]
        self.index += 2
        return int(num)

    def read_int(self):
        num = struct.unpack_from(">i", self.stream, self.index)[0]
        self.index += 4
        return int(num)

    def read_string(self):
        str_length = self.read_short()
        str = self.stream.decode("ISO-8859-1")[self.index:self.index + str_length]
        self.index += str_length
        return str