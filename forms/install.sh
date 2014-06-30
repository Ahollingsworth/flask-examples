#!/usr/bin/env bash

APP_NAME=forms
APP_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME
INDEX_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME/templates/index.html
ME_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME/templates/me.html

cd ~
mkdir -p $APP_NAME
cd $APP_NAME
[ -f $APP_NAME.py ] && rm $APP_NAME.py
curl -s $APP_URL > $APP_NAME.py
mkdir -p templates
[ -f templates/index.html ] && rm templates/index.html
curl -s $INDEX_URL > templates/index.html
[ -f templates/me ] && rm templates/me
curl -s $ME_URL > templates/me.html

echo "To run this app, type: 'cd && python $APP_NAME/$APP_NAME.py'"
