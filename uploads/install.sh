#!/usr/bin/env bash

APP_NAME=uploads
APP_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME
INDEX_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME/templates/index.html

cd ~
mkdir -p $APP_NAME
cd $APP_NAME
[ -f $APP_NAME.py ] && rm $APP_NAME.py
curl $APP_URL > $APP_NAME.py
mkdir -p templates
[ -f templates/index.html ] && rm -rf templates/index.html
curl -s $INDEX_URL > templates/index.html

mkdir -p static

echo "To run this app, type: 'cd && python $APP_NAME/$APP_NAME.py'"
