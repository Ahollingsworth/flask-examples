from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    # The 'index.html' template includes the text `{% name %}`,
    # which will be replaced by the value given below.
    # To change the output of the template to display a name other
    # than 'Robot', change the code below, like so:
    return render_template('index.html', name="Teacher")

# Teacher example route
@app.route("/teacher")
def teacher():
    return render_template('teacher.html', name="Teacher", age=30, cat_color="black")

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
