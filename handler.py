import json
# import os
# from datetime import datetime
# from bson.son import SON

# import pandas as pd
# from pandas import json_normalize
# import json

# from flask_cors import CORS
# from flask_pymongo import PyMongo
# from flask import jsonify
# from flask import request
# from flask import Flask

# app = Flask(__name__)
# cors = CORS(app, resources={r"/*": {"origins": "*"}})
# app.config.from_mapping(
#     # MONGO_URI="mongodb://localhost:27017/" + dbname,
#     # MONGO_URI="mongodb://cross2020:cross2020@docdb-2020-03-25-02-18-11.cluster-cl1egjscp0e8.us-west-2.docdb.amazonaws.com:27017/" + dbname + "?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false",
#     MONGO_URI="mongodb://cross2020:cross2020@docdb-2020-03-25-02-18-11.cluster-cl1egjscp0e8.us-west-2.docdb.amazonaws.com:27017/" + dbname
# )
# mongo = PyMongo(app)


def hello(event, context):
    body = {
        "message": "ZX ZX ZX, Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """

def home(event, context):
    # ## Default: Test mongo connection
    # mgdoc = mongo.db[collectionname].find(
    #     {
    #         "pickup_minute": 1430
    #     },
    #     {'_id': 0}
    # ).limit(1)

    body = {
        "message": "ZX ZX ZX, Go Serverless v1.0! Your function executed successfully!",
        "input": event
    }
    
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response
