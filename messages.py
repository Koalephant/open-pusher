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
            "args":{"postit_id":args["postit_id"], "x":args["x"], "y":args["y"]}
        }
        for handle in self.boards_controller.get_board_handles(args["channel_id"]):
            handle.write_message(json.dumps(moving_message))

    def new(self, handle, args):
        new_message = {
            "type":"new",
            "args":{"obj":"postit","postit_id":args["postit_id"], "x":args["x"], "y":args["y"], "text":args["text"]}
        }
        for handle in self.boards_controller.get_board_handles(args["channel_id"]):
            handle.write_message(json.dumps(new_message))