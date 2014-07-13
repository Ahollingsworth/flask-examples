from flask import Flask, render_template
app = Flask(__name__)

# There are two routes defined. Each one
# is handled by the same handler (the `hello` method).
# In addition, flask will intercept any characters after the
# "/" and store those in a variable called "name"
@app.route("/")
@app.route("/<name>")
def hello(name=None):
    # This sets a default value for name to "Robot"
    if name == None:
        name = "Robot"
    # If the name is "secret",
    # then render a different template:
    if name == "secret":
        return render_template('secret.html')
    return render_template('index.html', name=name)

# This makes it so visiting /cows/3 creates a page that says:
# "There are 3 cows", and also so that visiting "/frogs/11" it says
# "There are 11 frogs"
@app.route("/<animal>/<count>")
def animals(animal=None, count=None):
    return "There are " + count + " " + animal + "s"


if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
