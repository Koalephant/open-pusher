import tornado
from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.websocket import WebSocketHandler

GLOBALS={
    'sockets': []
}

class WSHandler(WebSocketHandler):
    def open(self):
        print 'connection established'
        GLOBALS['sockets'].append(self)

    def on_message(self, message):
        for handle in GLOBALS['sockets']:
            handle.write_message(message)

    def on_close(self):
        GLOBALS['sockets'].remove(self)
        print 'connection closed'

application = Application([
    (r'/ws', WSHandler),
])

if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()