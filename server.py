import tornado
from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.websocket import WebSocketHandler
from boards import BoardsController
from messages import MessageParser

boards_controller = BoardsController()

class BoardSyncHandler(WebSocketHandler):

    def __init__(self):
        self.message_parser = MessageParser(None)

    def open(self):
        pass

    def on_message(self, message):
        pass#boards_controller.on_message(message)

    def on_close(self):
        pass#boards_controller.unregister(self)

application = Application([
    (r'/ws', BoardSyncHandler),
])

if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()