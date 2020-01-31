from flask import Flask

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
import datetime
from config import MONGO_CONNECTION
# connect to MongoDB, change the \
# << MONGODB URL >> to reflect your own connection string


app = Flask(__name__)


@app.route("/")
def hello():
    client = MongoClient(MONGO_CONNECTION)
    databases = client.list_database_names()
    for database in databases:
        # databases
        pprint("database::" + str(database))
    return str(database)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port='5011',debug=True)
