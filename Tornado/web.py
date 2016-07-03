# coding = utf-8
import tornado.ioloop
import tornado.web
import os

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render( "template/index.html" )

class ApiDemoHandler(tornado.web.RequestHandler):
    def get(self):
        print("Handled by ApiDemoHandler")
        result = dict( msg = "Success" )
        self.write( result )



def make_app():
    return tornado.web.Application([
        (r"/index", MainHandler),
        (r"/api/index", ApiDemoHandler),
        (r"/js/(.*)", tornado.web.StaticFileHandler, {"path": os.getcwd() }),
        (r"/css/(.*)", tornado.web.StaticFileHandler, {"path": os.getcwd() }),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    print("Start Listening port:8888")
    print( os.getcwd() )
    tornado.ioloop.IOLoop.current().start()
