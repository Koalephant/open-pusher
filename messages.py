import json

class MessageParser(object):
    def __init__(self, message_handler):
        self.message_handler = message_handler

    # Parse a json file to get channel_id and look the type of decoded message received
    def parse(self, handle, message):
        decoded_message = json.loads(message)
        if decoded_message['type'] == 'register':
            self.message_handler.register(handle, decoded_message)
        self.message_handler.handle(decoded_message, handle)


class MessageHandler(object):

    def __init__(self, boards_controller):
        self.boards_controller = boards_controller

    def register(self, handle, decoded_message):
        channel_id = decoded_message['args']['channel_id']
        connected_users = self.boards_controller.count_users(channel_id)
        self.boards_controller.register(decoded_message, handle)
        users = self.boards_controller.get_board_users(channel_id)
        message = Message("info", {"connected_users":connected_users, "users":users})
        handle.send(message.as_json())

    # Get the message information and publish it in the board
    def handle(self, decoded_message, source):
        message = Message(decoded_message['type'],decoded_message['args'])
        channel_id = decoded_message['args']['channel_id']
        self.publish(message, channel_id, source)

    def publish(self, message, channel_id, excluded_handle=None):
        for board_handle in self.boards_controller.get_board_handles(channel_id):
            if board_handle!=excluded_handle:
                board_handle.send(json.dumps(message.as_dict()))


# Message Class
class Message(object):

    def __init__(self, type, args=None):
        self.type = type
        self.args = args

    def as_dict(self):
        return {"type":self.type, "args": self.args}

    def as_json(self):
        return json.dumps(self.as_dict())
