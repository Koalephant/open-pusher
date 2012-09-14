import tornadio2
from tornadio2.server import SocketServer
import tornado
from tornado.web import Application
from boards import BoardsController

boards_controller = BoardsController()


class MyConnection(tornadio2.SocketConnection):

    def on_message(self, message):
        boards_controller.on_message(self, message)

    def on_close(self):
        boards_controller.unregister(self)

class WebSocketsServer:

    def __init__(self, uri, port):

        MyRouter = tornadio2.TornadioRouter(MyConnection)

        application = Application(MyRouter.urls, socket_io_port = port)
        self.http_server = SocketServer(application, auto_start = False)

    def start(self):
        io_loop = tornado.ioloop.IOLoop.instance()
        io_loop.start()

    def stop(self):
        self.http_server.stop()
        tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
    server = WebSocketsServer(r'/ws', 8888)
    server.start()
