import json

class MessageParser(object):
    def __init__(self, message_handler):
        self.message_handler = message_handler

    def parse(self, handle, message):
        decoded_message = json.loads(message)
        getattr(self.message_handler, decoded_message['type'])(handle, decoded_message['args'])


class MessageHandler(object):

    def __init__(self, boards_controller):
        self.boards_controller = boards_controller

    def register(self, handle, args):
        self.boards_controller.register(args['channel_id'], handle)

    def move(self, handle, args):
        moving_message = {
            "type":"move",
            "args":args
        }
        self.publish(moving_message, args["channel_id"], handle)

    def new(self, handle, args):
        new_message = {
            "type":"new",
            "args":args
        }
        self.publish(new_message, args["channel_id"])


    def select(self, handle, args):
        select_message = {
            "type":"select",
            "args":args
        }
        self.publish(select_message, args["channel_id"], handle)

    def deselect(self, handle, args):
        deselect_message = {
            "type":"deselect",
            "args":args
        }
        self.publish(deselect_message, args["channel_id"], handle)

    def publish(self, message, channel_id, excluded_handle=None):
        for board_handle in self.boards_controller.get_board_handles(channel_id):
            if board_handle!=excluded_handle:
                board_handle.write_message(json.dumps(message))