from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        name = request.form['your_name']
        text = request.form['blog_post']

        post = {'name': name, 'text': text}
        write_post(post)

    posts = read_posts()

    return render_template('index.html', all_posts=posts)

def read_posts():
    posts = []

    dirname, filename = os.path.split(os.path.abspath(__file__))
    file_path = os.path.join(dirname, "posts.txt")

    if os.path.exists(file_path):
        file = open(file_path)

        for line in file:
            name, text = line.split("::")
            posts.append({'name': name, 'text': text})

        file.close()

    return posts

def write_post(post):
    dirname, filename = os.path.split(os.path.abspath(__file__))
    file_path = os.path.join(dirname, "posts.txt")

    encoded = "%(name)s::%(text)s\n" % post

    file = open(file_path, 'a')
    file.write(encoded)
    file.close()

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
