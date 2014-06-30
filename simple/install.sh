#!/usr/bin/env bash

APP_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/simple/
APP_NAME=simple

cd ~
mkdir -p $APP_NAME
cd $APP_NAME
[ -f ./$APP_NAME.py ] && rm ./$APP_NAME.py
curl -s $APP_URL/$APP_NAME.py > $APP_NAME.py

echo "To run this app, type: 'cd && python $APP_NAME/$APP_NAME.py'"
