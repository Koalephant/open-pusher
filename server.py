import tornado
from tornado.httpserver import HTTPServer
from tornado.web import Application
from tornado.websocket import WebSocketHandler

GLOBALS={
    'sockets': []
}

class WSHandler(WebSocketHandler):
    def open(self):
        print 'new connection'
        self.write_message("Hello World")
        GLOBALS['sockets'].append(self)

    def on_message(self, message):
        print 'Esta? :'
        print (self in GLOBALS['sockets'])
        print 'message received %s' % message

    def on_close(self):
        print 'connection closed'

application = Application([
    (r'/ws', WSHandler),
])

if __name__ == "__main__":
    http_server = HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()