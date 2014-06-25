#!/usr/bin/env bash

APP_NAME=routes
APP_URL="https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME/app.py"

cd ~
mkdir -p $APP_NAME
cd $APP_NAME
[ -f ./app.py ] && rm ./app.py
curl -s $APP_URL > app.py

echo "To run this app, type: 'cd && python $APP_NAME/app.py'"
