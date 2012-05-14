from messages import MessageParser, MessageHandler

class BoardsController(object):

    def __init__(self):
        self.boards = {}
        self.message_parser = MessageParser(MessageHandler(self))

    def register(self, channel_id, handle):
        if channel_id in self.boards.keys():
            self.boards[channel_id].append(handle)
        else:
            self.boards[channel_id] = [handle]

    def unregister(self, channel_id, handle):
        self.boards[channel_id].remove(handle)

    def get_board_handles(self, channel_id):
        return self.boards.get(channel_id)

    def on_message(self, handle, message):
        self.message_parser.parse(handle, message)
  