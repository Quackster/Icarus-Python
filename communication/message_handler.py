import util.logging as log
import game


def parse(session, incoming_message):
    """
    Parse incoming data from client
    :param session: the session who is currently connected
    :param incoming_message: the message to parse
    :return:
    """
    message = incoming_message[4:][:int(incoming_message[:4])]

    message_parts = message.split(' ')

    message_header = message_parts[0]
    message_data = message[len(message_header) + 1:] # Message without the header

    log.info("Incoming message (" + message_header + "): " + message_data)

    game.messages.incoming_message(session, message_header, message_data)