#!/usr/bin/env bash

APP_NAME=static
APP_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME
INDEX_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME/templates/index.html
FOOTBALL_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME/static/football.jpg
ISLAND_URL=https://raw.githubusercontent.com/NYC-DOE/flask-examples/master/$APP_NAME/static/island.jpg

cd ~
mkdir -p $APP_NAME
cd $APP_NAME
[ -f $APP_NAME.py ] && rm $APP_NAME.py
curl $APP_URL/$APP_NAME.py > $APP_NAME.py
mkdir -p templates
[ -f templates/index.html ] && rm -rf templates/index.html
curl -s $INDEX_URL > templates/index.html

mkdir -p static

[ -f static/football.jpg ] && rm static/football.jpg
[ -f static/island.jpg ] && rm static/island.jpg

curl -s $FOOTBALL_URL > static/football.jpg
curl -s $ISLAND_URL > static/island.jpg

echo "To run this app, type: 'cd && python $APP_NAME/$APP_NAME.py'"
