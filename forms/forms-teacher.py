from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/teacher")
def teacher():
    return render_template('teacher.html')

# This is the first time we've seen 'methods' keyword argument
# to the `@app.route` method call. In this case we are declaring
# an array of possible methods that the flask app will accept
# from a browser for the given url.
# The default method is 'GET', so we only need to add this
# keyword argument if we are declaring a method or methods other
# than the GET default.
@app.route("/myform", methods=['GET', 'POST'])
def form():
    # `request.values` will read values from a form, whether
    # they are sent via GET request of POST request
    name = request.values['name']
    age  = request.values['age']
    color = request.values['color']

    # Now that we have captured the form values into the
    # variables `name` and `age`, we pass those on to the
    # `render_template` method and display them in the
    # resulting page.
    return render_template('me-teacher.html', name=name, age=age, color=color)

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
