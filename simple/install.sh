#!/usr/bin/ sh

APP_URL=http://google.com/

cd ~
mkdir simple
cd simple
curl -s $APP_URL > simple/app.py

echo "To run this app, type: 'python simple/app.py'"
