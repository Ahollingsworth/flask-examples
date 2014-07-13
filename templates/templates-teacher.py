from flask import Flask, render_template
# Note that in addition to "Flask",
# "render_template" is also imported

app = Flask(__name__)

@app.route("/")
def hello():
    # render_template renders the template that is found in the
    # relative directory "templates/" and that matches the name
    # of the string provided, so
    # this method will render the template "index.html" in
    # "templates/"
    # Editing the "index.html" template file will change what is
    # displayed when the user visits the route ("/")
    return render_template('index.html')

@app.route("/teacher")
def teacher():
    # See the template in "templates/teacher.html" for more information
    # on how to change the page title and so on.
    #
    # More documentation about flask's usage of 'render_template' is
    # here: http://flask.pocoo.org/docs/quickstart/#rendering-templates
    #
    # Flask uses the 'jinja2' templating library. The documentation for
    # jinja2 is here: http://jinja.pocoo.org/docs/
    return render_template('teacher.html')

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
