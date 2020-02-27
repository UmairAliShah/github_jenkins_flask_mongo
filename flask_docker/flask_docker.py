from flask import Flask
from flask import request
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


@app.route("/insert-data", methods['PUT'])
def hello():
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]
    mydict = { "name": "John", "address": "Highway 37" }
    x = mycol.insert_one(mydict)
    databases = client.list_database_names()
    for database in databases:
        # databases
        pprint("database::" + str(database))
    return str(x)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5011',debug=True)
