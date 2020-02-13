#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Flask Quickstart
subtitle: URL Building
version: 1.0
type: example
keywords: [url_from, test_request_context, Flask, REST API]   # there are always some keywords!
description: |
remarks:
todo:
sources:
    - title: Flask Quickstart
      link: https://flask.palletsprojects.com/en/1.1.x/quickstart/#url-building
      usage: copy
file:
    usage:
        interactive: True   # if the file is intended to be run interactively e.g. in Spyder
        terminal: True     # if the file is intended to be run in a terminal
    name: 10-quickstart-url_building.py
    path: D:/ROBOCZY/Python/REST/Flask
    date: 2019-12-07
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%%
from flask import Flask, escape, url_for

#%%
app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

#%%

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='A K'))

#%%
