#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Creating a REST API
subtitle:
version: 1.0
type: example
keywords: [Flask, REST API]   # there are always some keywords!
description: |
remarks:
todo:
sources:
    - title: This is how easy it is to create a REST API
      link: https://codeburst.io/this-is-how-easy-it-is-to-create-a-rest-api-8a25122ab1f3
      author:
          - fullname: Leon Wee
      date: 2018-03-08
      usage: copy
file:
    usage:
        interactive: False   # if the file is intended to be run interactively e.g. in Spyder
        terminal: True     # if the file is intended to be run in a terminal
    name: rest1.py
    path: D:/ROBOCZY/Python/REST/rest1/
    date: 2019-12-07
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - arek@staart.pl
              - akasp666@google.com
"""
#%%
"""
cd %PYWORKS%\REST\rest1\
cd

> $env:FLASK_APP = "rest1.py"   # PowerShell

REM cmd
setx FLASK_APP rest1.py
setx FLASK_ENV development
setx FLASK_DEBUG 1
refreshenv

flask run --host=127.0.0.1:5000     & :: default host:port
python -m flask run

flask run --host=0.0.0.0    #  externally visible server
"""

#%%
from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

#%%

users = [{"name": "Nyarlathotep", "age": 42, "occupation": "doctor"},
         {"name": "Bolek", "age": 55, "occupation": "web dev"},
         {"name": "Zenon", "age": 32, "occupation": "net engineer"},
         {"name": "Janusz", "age": 28, "occupation": "teacher"},
         {"name": "Grzegorz", "age": 63, "occupation": "seller"}
        ]

#%%

class User(Resource):

    def get(self, name):
        for user in users:
            if(name == user["name"]):
                return user, 200

    def post(self, name):
        """to create new user
        """
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                return "User with name {} already exists.".format(name), 400

        user = {"name": name,
                "age": args["age"],
                "occupation": args["occupation"]
               }

        users.append(user)
        return user, 201

    def put(self, name):
        """to update user
        """
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()

        for user in users:
            if(name == user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200

        user = {"name": name,
                "age": args["age"],
                "occupation": args["occupation"]
               }

        users.append(user)
        return user, 201


    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "User {} deleted".format(name), 200

class Users(Resource):

    def get(self):
        return users, 200

#%%

api.add_resource(User, "/user/<string:name>")
api.add_resource(Users, "/users/")

app.run()


