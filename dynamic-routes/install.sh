#!/usr/bin/env bash

APP_NAME=dynamic-routes
APP_URL="https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME/app.py"
INDEX_URL="https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME/templates/index.html"

cd ~
mkdir -p $APP_NAME
cd $APP_NAME
[ -f app.py ] && rm app.py
curl $APP_URL > app.py
mkdir -p templates
[ -f templates/index.html ] && rm -rf templates/index.html
curl -s $INDEX_URL > templates/index.html

echo "To run this app, type: 'cd && python $APP_NAME/app.py'"
