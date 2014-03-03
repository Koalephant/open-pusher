import tornadio2
from tornadio2.server import SocketServer
import tornado
from tornado.web import Application
from boards import BoardsController

boards_controller = BoardsController()

# MyConnection Class
class MyConnection(tornadio2.SocketConnection):

    def on_message(self, message):
        boards_controller.on_message(self, message)

    def on_close(self):
        boards_controller.unregister(self)

class WebSocketsServer:

    def __init__(self, uri, port):
        # Creating a Tornadio2 server for the connection
        MyRouter = tornadio2.TornadioRouter(MyConnection)

        application = Application(MyRouter.urls, socket_io_port = port)
        self.http_server = SocketServer(application, auto_start = False)

    # Start Tornadio2 server
    def start(self):
        io_loop = tornado.ioloop.IOLoop.instance()
        io_loop.start()

    # Stop Tornadio2 server
    def stop(self):
        self.http_server.stop()
        tornado.ioloop.IOLoop.instance().stop()

if __name__ == "__main__":
    # Port listening (8888)
    server = WebSocketsServer(r'/ws', 80)
    server.start()
