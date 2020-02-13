#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Building a Basic RestFul API in Python
subtitle:
version: 1.0
type: example
keywords: [SQLAlchemy, SQLite, Flask, REST API]   # there are always some keywords!
description: |
    Basic example of building REST API with Flask
remarks:
todo:
sources:
    - title: Building a Basic RestFul API in Python
      link: https://www.codementor.io/sagaragarwal94/building-a-basic-restful-api-in-python-58k02xsiq
      date: 2017-02-13
      authors:
          - fullname: Sagar Chand Agarwal
      usage: copy
file:
    usage:
        interactive: False   # if the file is intended to be run interactively e.g. in Spyder
        terminal: True     # if the file is intended to be run in a terminal
    name: rest0.py
    path: D:/ROBOCZY/Python/REST/
    date: 2019-12-07
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""


#%%

# import flask
from sqlalchemy import create_engine
from flask_restful import Resource, Api
from flask import Flask, request
from json import dumps
from flask_jsonpify import jsonify

#%%

db_connect = create_engine('sqlite:///chinook.db')

#%%
class Employees(Resource):
    def get(self):
        conn = db_connect.connect()  # connect to DB
        query = conn.execute("SELECT * FROM employees")
        #result = {'employees': [i for i in query.cursor]}
        #result = {'employees': [query.keys() for i in query.cursor]}
        #result = {'employees': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        result = {'employees': [dict(zip(query.keys(), i)) for i in query.cursor]}
        return result

class Tracks(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("SELECT trackid, name, composer, unitprice FROM tracks")
        result = {'data': [dict(zip(query.keys(), i)) for i in query.cursor]}
        return result

class EmployeesName(Resource):
    def get(self, employee_id):
        conn = db_connect.connect()
        query = conn.execute("SELECT * FROM employees WHERE EmployeeId={}".format(employee_id))
        result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)

#%%

app = Flask(__name__)
api = Api(app)

api.add_resource(Employees, '/employees')  # route 1
api.add_resource(Tracks, '/tracks')  # route 2
api.add_resource(EmployeesName, '/employees/<employee_id>')  # route 3

#%%

if __name__ == "__main__":
    app.run(port='5003')


#%%
