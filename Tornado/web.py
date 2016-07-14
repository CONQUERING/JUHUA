# coding = utf-8
import tornado.ioloop
import tornado.web
import os
import hashlib
import json
import time
from pymongo import MongoClient
from bson.objectid import ObjectId
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test

class RegisterHandler(tornado.web.RequestHandler):
    def get(self):
        self.render( "template/register.html" )

class ApiRegisterHandler(tornado.web.RequestHandler):
    def post(self):
        s_id = self.get_secure_cookie( name = "session_id" )
        print(s_id)
        email = self.get_body_argument(name = "email")
        password = self.get_body_argument(name = "password")
        # password = h.update(password.encode())
        password = password.encode("utf8")
        password = hashlib.sha1(password).hexdigest()
        users = db.users
        _result = users.find_one({"email":email})
        if _result==None:
            print(email,password)
            import datetime
            user = {
                    # "_id": mail,
                    "email":email,
                    "password":password,
                    "date":datetime.datetime.utcnow()
            }
            try:
                post_id = users.insert_one(user).inserted_id
                response = {
                    "error_code" : 0,
                    "err_msg"   : "",
                    "user_id"   : "{}".format(post_id),
                    "email"     : email,
                }
                self.set_secure_cookie( name= "session_id" , value = "lalala" )
                self.write( json.dumps(response) )
            except Exception as e:
                print(e)
                self.write( "Failed" )
            print( post_id )
        else:
            self.write('Your email address is occupied')

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render( "template/login.html" )

class ApiLoginHandler(tornado.web.RequestHandler):
    def post(self):
        email = self.get_body_argument(name = "mail")
        password = self.get_body_argument(name = "password")
        password = h.update(password.encode())
        print(mail,password)
        users = db.users
        _result = users.find_one({"email":email}and{"password":password})
        if _result==None:
            self.write('Welcome,'+ email+'!')
        else:
            self.write('Your login is invalid')

application = tornado.web.Application([
        (r"/register",RegisterHandler),
        (r"/api/register",ApiRegisterHandler),
        (r"/login",LoginHandler),
        (r"/api/login",ApiLoginHandler),
        (r"/js/(.*)",tornado.web.StaticFileHandler, {"path": os.getcwd()+'/js/' }),
        (r"/css/(.*)",tornado.web.StaticFileHandler, {"path": os.getcwd()+'/css/' }),
        ], cookie_secret= str( time.time() )
        )

if __name__ == "__main__":
    application.listen(8888)
    print("Start Listening port:8888")
    print( os.getcwd() )
    tornado.ioloop.IOLoop.current().start()
