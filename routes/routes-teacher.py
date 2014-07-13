from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

@app.route("/about")
def about():
    # return "About me"
    # Changing to return more info about me
    return "My name is Sparkles. I'm a cat"

#
# Here is an example of adding a 3rd route, the url "/cats"
#
@app.route("/cats")
def cats(): # The method name matches the route by convention
    return "This page is about all the cats"

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
