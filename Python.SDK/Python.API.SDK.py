from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello world'}
    def post(self):
        return {'about': 'Hello world with post'}

class Modify(Resource):
    def get(self, num):
        return {'about': num * 10}

api.add_resource(HelloWorld, '/')
api.add_resource(Modify, '/modify/<int:num>')

if __name__ == "__main__":
    app.run(host="0.0.0.0")