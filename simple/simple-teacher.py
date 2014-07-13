from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    # The name of the function above does not matter, but it does need
    # *a* name.
    # For instance, this will not work: `def ():`
    #
    # Whatever string is returned by this function will be
    # displayed on the page.
    # Other examples:
    #  return "Some more text"
    #  return "<h1>This is HTML</h1>"
    return "Hello world!"

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
