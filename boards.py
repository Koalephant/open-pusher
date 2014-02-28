from messages import MessageParser, MessageHandler, Message

# Boards Controller
class BoardsController(object):

    # Generate a Boards instance
    def __init__(self):
        self.boards = {}
        self.message_handler = MessageHandler(self)
        self.message_parser = MessageParser(self.message_handler)

    # Add a board to the Boards instances
    def register(self, channel_id, handle):
        if channel_id in self.boards.keys():
            self.boards[channel_id].append(handle)
        else:
            self.boards[channel_id] = [handle]

    # Remove a board to the Boards instances
    def unregister(self, handle, channel_id=None):
        if channel_id is None:
            for channel_id in self.boards:
                if handle in self.boards[channel_id]:
                    self.boards[channel_id].remove(handle)
                    self.message_handler.publish(Message("disconnect"),channel_id)
        else:
            self.boards[channel_id].remove(handle)
            self.message_handler.publish(Message("disconnect"),channel_id)

    # Get a specific board
    def get_board_handles(self, channel_id):
        return self.boards.get(channel_id)

    # Get number of users that are in the board at the moment
    def count_users(self, channel_id):
        if channel_id in self.boards.keys():
            return len(self.boards.get(channel_id))
        return 0

    def on_message(self, handle, message):
        self.message_parser.parse(handle, message)
  