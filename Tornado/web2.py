# coding = utf-8
import tornado.ioloop
import tornado.web
import os

from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render( "template/login.html" )

class ApiLoginHandler(tornado.web.RequestHandler):
    def post(self):
        mail = self.get_body_argument(name = "mail")
        password = self.get_body_argument(name = "password")
        print(mail,password)
        import datetime
        user = {
                    # "_id": mail,
                    "email": mail,
                    "password":password,
                    "date":datetime.datetime.utcnow()
                }
        users = db.users
        post_id = users.insert_one(user).inserted_id
        print( post_id )
        if mail == "834931501@qq.com" and password == ".juyuhuifbi":
            self.write( 'Success' )
        else:
            self.write( 'Username and Password don\'t match' )


application = tornado.web.Application([
        (r"/login",LoginHandler),
        (r"/api/login",ApiLoginHandler)
        (r"/js/(.*)",tornado.web.StaticFileHandler, {"path": os.getcwd()+'/js/' }),
        (r"/css/(.*)",tornado.web.StaticFileHandler, {"path": os.getcwd()+'/css/' }),
        ])

if __name__ == "__main__":
    application.listen(8888)
    print("Start Listening port:8888")
    print( os.getcwd() )
    tornado.ioloop.IOLoop.current().start()
