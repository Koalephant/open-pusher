import unittest
from mock import MagicMock
from boards import BoardsController


class BoardsControllerTest(unittest.TestCase):

    def test_register(self):
        boards = BoardsController()
        channel_id = "xxx"
        handle = MagicMock()
        boards.register(channel_id, handle)
        assert handle in boards.get_board_handles(channel_id)

    def test_unregister_handle(self):
        boards = BoardsController()
        channel_id = "xxx"
        handle = MagicMock()
        boards.register(channel_id, handle)
        boards.unregister(channel_id, handle)
        assert handle not in boards.get_board_handles(channel_id)

    def test_routing_message_to_right_channel(self):
        pass

