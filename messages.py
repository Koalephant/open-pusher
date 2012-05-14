import json

class MessageParser(object):
    def __init__(self, message_handler):
        self.message_handler = message_handler

    def parse(self, message):
        decoded_message = json.loads(message)
        getattr(self.message_handler, decoded_message['type'])()