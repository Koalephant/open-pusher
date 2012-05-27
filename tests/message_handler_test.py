import unittest
from mock import MagicMock
from messages import MessageParser

class MessageHandlerTest(unittest.TestCase):

    def setUp(self):
        self.handle = MagicMock()
        self.message_handler = MagicMock()
        self.message_parser = MessageParser(self.message_handler)

    def test_parsing_register_message(self):
        self.message_parser.parse(self.handle, '{"type":"register", "args": {}}')

        self.message_handler.register.assert_called_with(self.handle, {})

    def test_parsing_new_message(self):
        self.message_parser.parse(self.handle, '{"type":"new", "args": {}}')

        self.message_handler.new.assert_called_with(self.handle, {})

    def test_parsing_postit_moved_message(self):
        self.message_parser.parse(self.handle, '{"type":"move", "args": {}}')
        self.message_handler.move.assert_called_with(self.handle, {})

    def test_move_is_not_call_with_register_message(self):
        self.message_parser.parse(self.handle, '{"type":"register", "args": {}}')

        assert self.message_handler.move.call_count == 0

    def test_register_message_with_arguments(self):
        self.message_parser.parse(self.handle, '{"type":"register", "args": {"channel_id":1}}')

        self.message_handler.register.assert_called_with(self.handle, {'channel_id':1})


