#!/usr/bin/env bash

APP_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/simple/app.py

cd ~
mkdir -p simple
cd simple
touch app.py
curl -s $APP_URL > app.py

echo "To run this app, type: 'python simple/app.py'"
