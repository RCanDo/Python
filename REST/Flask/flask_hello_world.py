#! python3
# -*- coding: utf-8 -*-
"""
---
# This is YAML, see: https://yaml.org/spec/1.2/spec.html#Preview
# !!! YAML message always begin with ---

title: Flask Hello World
subtitle:
version: 1.0
type: example
keywords: [Flask, REST API]   # there are always some keywords!
description: |
remarks:
todo:
sources:
    - title: Flask
      link: https://palletsprojects.com/p/flask/
      usage: copy
file:
    usage:
        interactive: False   # if the file is intended to be run interactively e.g. in Spyder
        terminal: True     # if the file is intended to be run in a terminal
    name: flask_helo_world.py
    path: D:/ROBOCZY/Python/REST/Flask/
    date: 2019-12-07
    authors:
        - nick: rcando
          fullname: Arkadiusz Kasprzyk
          email:
              - akasp666@google.com
              - arek@staart.pl
"""
#%%
"""
cd %PYWORKS%\REST\Flask\

> $env:FLASK_APP = "flask_hello_world.py"   # PowerShell

REM cmd
setx FLASK_APP flask_hello_world.py
setx FLASK_ENV development
setx FLASK_DEBUG 1
refreshenv


flask run --host=127.0.0.1:5000    & :: default host:port
python -m flask run

flask run --host=0.0.0.0    #  externally visible server
"""

#%%

from flask import Flask, escape, request
app = Flask(__name__)

@app.route('/hello/<arg>')
def hello(arg):
    name = request.args.get("name", arg)
    return f'Hello, {escape(name)}! Is that OK?'

if __name__ == "__main__":
    app.run()