from flask import Flask, Response
from flask_restful import Resource, Api, reqparse
from algorithms.InsertionSort import InsertionSort
from algorithms.utility import GenerateRandomArray
from flask_cors import CORS

app=Flask(__name__)
api=Api(app)

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

class Algorithm(Resource):
    def get(self, name):

        if(name=="InsertionSort"):
            Array=GenerateRandomArray(10)
            BigArray=InsertionSort(Array)
            return BigArray,200

        return "User not found", 404

    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args=parser.parser_args()

        for user in users:
            if(name==user["name"]):
                return "User with name {} already exists".format(name), 400

        user={
            "name": name,
            "age": args["age"],
            "occupation": args
        }

    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args= parser.parsea_args()

        for user in users:
            if(name==user["name"]):
                user["age"] = args["age"]
                user["occupation"] = arg["occupation"]
                return user, 200, {'Access-Control-Allow-Origin': '*'}

        user={
            "name": name,
            "age": args["age"],
            "occupation": args["occupation"]
        }

        users.append(user)
        return user, 201

    def delete(self, name):
        global users
        users=[user for user in users if user["name"]!=name]
        return "{} is deleted".format(name), 200

api.add_resource(Algorithm, "/api/algorithm/<string:name>")
app.run(debug=True)
