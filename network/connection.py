import asyncore
import communication.message_handler as message_handler


class Connection(asyncore.dispatcher_with_send):

    def handle_read(self):
        data = self.recv(1024)
        connection = self
        if data:
            message_handler.parse(connection, data.decode())
        else:
            print("Socket disconnected")
            self.close()
