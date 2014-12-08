from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    # If POSTing new data, get it and save it
    if request.method == 'POST':
        name = request.form['your_name']
        text = request.form['blog_post']

        post = {'name': name, 'text': text}
        write_post(post)

    # on every request, whether we were posting new data or not,
    # read the posts from the file
    posts = read_posts()

    return render_template('index.html', all_posts=posts)

# We make this method here once rather than repeating the
# code in `read_posts` and `write_post`
def get_posts_file_path():
    # figure out the directory (folder) name of this file
    dirname, filename = os.path.split(os.path.abspath(__file__))

    # the file path is the file called "posts.txt" in this directory
    file_path = os.path.join(dirname, "posts.txt")


# open up "posts.txt" and read all the posts from it.
# posts are encoded as name::text, example:  "person::said something"
def read_posts():
    posts = []

    file_path = get_posts_file_path()

    # if the posts.txt file exists:
    if os.path.exists(file_path):
        file = open(file_path)

        # loop through each line, splitting it on the "::" separator
        for line in file:
            name, text = line.split("::")
            posts.append({'name': name, 'text': text})

        file.close()

    return posts

# Save a single post to the file
def write_post(post):
    file_path = get_posts_file_path()

    # encoded the post's name and text into a name::text string with a newline
    # at the end. "\n" denotes a new line.
    encoded = "%(name)s::%(text)s\n" % post

    # open the file in "append" mode, meaning we will add to its contents (at
    # the end) rather than overwriting its contents. The "a" signifies append mode.
    file = open(file_path, 'a')
    file.write(encoded)
    file.close()

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
