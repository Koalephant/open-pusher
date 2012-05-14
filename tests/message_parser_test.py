import unittest
from mock import MagicMock
from messages import MessageParser

class MessageParserTest(unittest.TestCase):

    def setUp(self):
        self.message_handler = MagicMock()
        self.message_parser = MessageParser(self.message_handler)

    def test_parsing_register_message(self):
        self.message_parser.parse('{"type":"register"}')
        self.message_handler.register.assert_called_with()


    def test_parsing_postit_moved_message(self):
        self.message_parser.parse('{"type":"move"}')
        self.message_handler.move.assert_called_with()


    def test_move_is_not_call_with_register_message(self):
        self.message_parser.parse('{"type":"register"}')
        self.message_handler.register.assert_called_with()
        assert self.message_handler.move.call_count == 0

