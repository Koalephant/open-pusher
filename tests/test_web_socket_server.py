import json
import threading
import unittest
from websocket import create_connection
from server import WebSocketsServer


class WebSocketServerTest(unittest.TestCase):

    def setUp(self):
        self.server = WebSocketsServer(r'/ws',8888)
        threading.Thread(target=self.start_tornado).start()

    def start_tornado(self):
        self.server.start()

    def tearDown(self):
        self.server.stop()

    def test_receving_move_message_from_same_channel(self):
        ws2 = create_connection("ws://localhost:8888/ws")
        ws2.send('{"type":"register","args":{"channel_id":"1"}}')

        ws = create_connection("ws://localhost:8888/ws")
        ws.send('{"type":"move","args":{"channel_id":"1","postit_id":2,"x":1,"y":2}}')

        received_message = json.loads(ws2.recv())
        expected_message = {"type":"move","args":{"postit_id":2,"x":1,"y":2}}

        ws2.close()
        ws.close()
        assert received_message == expected_message

    def test_receving_new_note_message_from_same_channel(self):
        ws2 = create_connection("ws://localhost:8888/ws")
        ws2.send('{"type":"register","args":{"channel_id":"1"}}')

        ws = create_connection("ws://localhost:8888/ws")

        ws.send('{"type":"new","args":{"channel_id":"1","obj":"postit","postit_id":2,"x":1,"y":2, "text":"Hola mundo"}}')

        received_message = json.loads(ws2.recv())
        expected_message = {"type":"new","args":{"postit_id":2,"obj":"postit","x":1,"y":2, "text":"Hola mundo"}}

        ws2.close()
        ws.close()

        assert received_message == expected_message


    def test_receving_select_message_from_same_channel(self):
        ws2 = create_connection("ws://localhost:8888/ws")
        ws2.send('{"type":"register","args":{"channel_id":"1"}}')

        ws = create_connection("ws://localhost:8888/ws")

        ws.send('{"type":"select","args":{"channel_id":"1","id":2}}')

        received_message = json.loads(ws2.recv())
        expected_message = {"type":"select","args":{"id":2}}

        ws2.close()
        ws.close()

        assert received_message == expected_message