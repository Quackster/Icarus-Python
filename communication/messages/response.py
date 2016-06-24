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

    def get_str_buffer(self):

        str_buffer = self.get_buffer().decode("utf8")



    def get_buffer(self):
        new_buffer = bytearray()
        new_buffer.extend(struct.pack(">i", len(self.buffer)))
        new_buffer.extend(self.buffer)
        return new_buffer