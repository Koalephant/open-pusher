from messages import MessageParser, MessageHandler, Message

class BoardsController(object):

    def __init__(self):
        self.boards = {}
        self.message_handler = MessageHandler(self)
        self.message_parser = MessageParser(self.message_handler)

    def register(self, decoded_message, handle):
        channel_id = decoded_message['args']['channel_id']
        if channel_id in self.boards.keys():
            self.boards[channel_id][handle] = decoded_message['args']['user']
        else:
            self.boards[channel_id] = {}
            self.boards[channel_id][handle] = decoded_message['args']['user']

    def unregister(self, handle, channel_id=None):
        if channel_id is None:
            for channel_id in self.boards:
                if handle in self.boards[channel_id]:
                    self.message_handler.publish(Message("disconnect",self.boards[channel_id][handle]),channel_id)
                    del self.boards[channel_id][handle]
        else:
            self.message_handler.publish(Message("disconnect",self.boards[channel_id][handle]),channel_id)
            del self.boards[channel_id][handle]

    def get_board_handles(self, channel_id):
        return self.boards.get(channel_id)

    def get_board_users(self, channel_id):
        print self.boards.get(channel_id)
        print channel_id
        return self.boards.get(channel_id).values()

    def count_users(self, channel_id):
        if channel_id in self.boards.keys():
            return len(self.boards.get(channel_id))
        return 0

    def on_message(self, handle, message):
        self.message_parser.parse(handle, message)
  