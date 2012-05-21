import tornado
from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.websocket import WebSocketHandler
from boards import BoardsController

boards_controller = BoardsController()

class BoardSyncHandler(WebSocketHandler):

    def open(self):
        print 'connection established'
        pass

    def on_message(self, message):
        print message
        boards_controller.on_message(self, message)

    def on_close(self):
        pass


class WebSocketsServer:

    def __init__(self, uri, port):
        application = Application([
            (uri, BoardSyncHandler),
        ])

        self.http_server = HTTPServer(application)
        self.http_server.listen(port)

    def start(self):
        io_loop = tornado.ioloop.IOLoop.instance()
        io_loop.start()

    def stop(self):
        self.http_server.stop()
        tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
    server = WebSocketsServer(r'/ws', 8888)
    server.start()
