# coding = utf-8
import pymongo
$ mongod
from pymongo import MongoClient
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.test
import datetime
post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()
posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id
db.collection_names(include_system_collections=False)
posts.find_one()

from bson.objectid import ObjectId

# The web framework gets post_id from the URL and passes it as a string
def get(post_id):
    # Convert from string to ObjectId:
    document = client.db.collection.find_one({'_id': ObjectId(post_id)})

new_posts = [{"author": "Mike",
               "text": "Another post!",
               "tags": ["bulk", "insert"],
               "date": datetime.datetime(2009, 11, 12, 11, 14)},
              {"author": "Eliot",
               "title": "MongoDB is fun",
               "text": "and pretty easy too!",
               "date": datetime.datetime(2009, 11, 10, 10, 45)}]
for post in posts.find():
   post

posts.count()
osts.find({"author": "Mike"}).count()
result = db.profiles.create_index([('user_id', pymongo.ASCENDING)],unique=True)
list(db.profiles.index_information())
# [u'user_id_1', u'_id_']
