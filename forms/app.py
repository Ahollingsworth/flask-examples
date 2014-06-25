from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/myform", methods=['GET', 'POST'])
def form():
    name = request.values['name']
    age  = request.values['age']
    return render_template('me.html', name=name, age=age)

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
