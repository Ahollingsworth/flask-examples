from flask import Flask, request, render_template
app = Flask(__name__)
posts = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['your_name']
        text = request.form['blog_post']

        posts.append({'name': name, 'text': text})
    return render_template('index.html', all_posts=posts)

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
