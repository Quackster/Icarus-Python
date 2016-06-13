import util.logging as log
import variables


def parse(session, incoming_message):

    message_length = int(incoming_message[:4])

    message = incoming_message[4:][:message_length]
    message_parts = message.split(' ')
    message_header = message_parts[0]
    message_data = message[len(message_header) + 1:] # Message without the header

    log.info("Incoming message (" + message_header + "): " + message_data)

    variables.messages.incoming_message(session, message_header, message_data)