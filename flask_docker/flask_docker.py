from flask import Flask
from flask import request
from bson.objectid import ObjectId
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import datetime
import os
import config as config
# connect to MongoDB, change the \
# << MONGODB URL >> to reflect your own connection string


app = Flask(__name__)
mongo = os.environ['mongo']
client = MongoClient(str(mongo)+config.MONGO_CONNECTION)


@app.route('/')
def hello():
    mydb = client["mydatabase"]
    mycol = mydb["customers"]
    mydict = { "name": "John", "address": "Highway 37" }
    x = mycol.insert_one(mydict)
    databases = client.list_database_names()
    for database in databases:
        # databases
        pprint("database::" + str(database))
    return str('200')

@app.route('/get')
def hello1():
    mydb = client["mydatabase"]
    mycol = mydb["customers"]
    myquery = { "address": "Highway 37"}
    mydoc = mycol.find_one(myquery)
    return mydoc
    


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5011',debug=True)
