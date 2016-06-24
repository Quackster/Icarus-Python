"""
Response class for sending packets back to client
Author: Alex (TheAmazingAussie)
"""

import struct


class Response:

    def __init__(self, header):
        self.header = header
        self.buffer = bytearray()
        self.index = 0

        self.write_short(header)

    def write_short(self, number):
        self.buffer.extend(struct.pack(">h", number))
        self.index += 2

    def write_int(self, number):
        self.buffer.extend(struct.pack(">i", number))
        self.index += 4
        
    def write_string(self, string):
        str_len = len(string)

        self.write_short(str_len)
        self.buffer.extend(bytes(string, "utf8"))

        self.index += str_len

    def write_bool_int(self, number):
        if number:
            self.write_int(1)
        else:
            self.write_int(0)

    def write_bool(self, number):
        if number:
            self.buffer.extend(1)
        else:
            self.buffer.extend(0)

        self.index += 1

    def get_buffer(self):
        new_buffer = bytearray()
        new_buffer.extend(struct.pack(">i", len(self.buffer)))
        new_buffer.extend(self.buffer)
        return new_buffer