import tornado.web
import tornado.wsgi
import tornado.ioloop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("PG aws test")

webApp = tornado.web.Application([
    (r"/", MainHandler),
])

application = tornado.wsgi.WSGIAdapter(webApp)

if __name__ == '__main__':
    webApp.listen(8000)
    tornado.ioloop.IOLoop.current().start()