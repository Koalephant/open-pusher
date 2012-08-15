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
        self.publish(Message("move", args), args["channel_id"], handle)

    def new(self, handle, args):
        self.publish(Message("new", args), args["channel_id"], handle)

    def select(self, handle, args):
        self.publish(Message("select", args), args["channel_id"], handle)

    def deselect(self, handle, args):
        self.publish(Message("deselect", args), args["channel_id"], handle)

    def delete(self, handle, args):
        self.publish(Message("delete", args), args["channel_id"], handle)

    def publish(self, message, channel_id, excluded_handle=None):
        for board_handle in self.boards_controller.get_board_handles(channel_id):
            if board_handle!=excluded_handle:
                board_handle.write_message(json.dumps(message.as_dict()))


class Message(object):
    def __init__(self, type, args):
        self.type = type
        self.args = args

    def as_dict(self):
        return {"type":self.type, "args": self.args}
