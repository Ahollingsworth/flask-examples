#!/usr/bin/env bash

APP_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/simple/app.py

cd ~
mkdir simple
cd simple
curl -s $APP_URL > simple/app.py

echo "To run this app, type: 'python simple/app.py'"
