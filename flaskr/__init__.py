'''
export FLASK_APP=flaskr
export FLASK_ENV=development

flask run --host 0.0.0.0 --port 20327
'''

dbname = "nyctaxi"
collectionname = "yellow_tripdata_2019_01"


import os
from datetime import datetime
from bson.son import SON
import json

from flask_cors import CORS
from flask_pymongo import PyMongo
from flask import jsonify
from flask import request
from flask import Flask


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_mapping(
        # MONGO_URI="mongodb://localhost:27017/" + dbname,
        MONGO_URI="mongodb://<username>:<userpassword>@docdb-2020-03-25-02-18-11.cluster-cl1egjscp0e8.us-west-2.docdb.amazonaws.com:27017/" + dbname + "?replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false",
        SECRET_KEY='dev',
        # DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    # app.config["MONGO_URI"] = "mongodb://localhost:27017/myDatabase"
    mongo = PyMongo(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    ## Default: Test mongo connection
    @app.route("/")
    def home_page():
        mgdoc = mongo.db[collectionname].find(
            {
                "pickup_minute": 1430
            },
            {'_id': 0}
        ).limit(1)

        # return render_template("index.html",
        #     online_users=online_users)
            
        return jsonify([cur for cur in mgdoc])


    ## Demo: GET
    ## http://localhost:5000/hello?key1=aaa&key2=bbb
    @app.route('/hello')
    def hello():
        args = request.args
        print (args) # For debugging
        no1 = args['key1']
        no2 = args['key2']
        return jsonify(dict(data=[no1, no2])) 


    # ## Section 1: For Operators
    # ## 1. 热门叫车地点的罗列 PULocationID/group_COUNT
    @app.route("/curhourbylocations10")
    def curhourbylocations10():
 
        weeekdaynow = datetime.today().weekday()
        daynow = datetime.now().day
        hournow = datetime.now().hour
        
        mgdoc = mongo.db[collectionname].aggregate([
                {"$match": {"pickup_hour": hournow, "pickup_day": daynow}},
                {
                    "$group":{
                    "_id": 
                            {
                            "PULocationID": "$PULocationID",
                            # "pickup_minute": "$pickup_minute", 
                            # "pickup_weekday": "$pickup_weekday"
                            },
                         
                    "group_COUNT": {"$sum": 1},
                    "total_amount_AVG": {"$avg": "$total_amount"},
                    "travel_time_AVG": {"$avg": "$travel_time"},
                    "travel_speed_AVG": {"$avg": "$travel_speed"}
                    }
                },
                {"$sort": SON([("group_COUNT", -1)])},
                {"$limit": 10}
            ])

        mgdoclist = []
        for cur in mgdoc:
            cur.update(cur.pop('_id'))
            mgdoclist.append(cur)

        return jsonify(dict(data=mgdoclist))


    return app