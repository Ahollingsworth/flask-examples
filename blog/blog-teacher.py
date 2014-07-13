from flask import Flask, request, render_template
app = Flask(__name__)
posts = []

@app.route('/teacher', methods=['GET', 'POST'])
def index():
    # If we POSTed data to this route, grab the name and
    # text variables (which are called 'your_name' and 'blog_post')
    # in the form, respectively
    if request.method == 'POST':
        name = request.form['your_name']
        text = request.form['blog_post']

        # Append a new python object with property values of 'name' and
        # 'text' (having values maching the `name` and `text` variables,
        # which correspond to the 'your_name' and 'blog_post' input
        # fields in the form).
        #
        # The `append` method adds a new item to the end of an array.
        # The `posts` array starts out as an empty array (on line 3).
        #
        # Each time we POST new form data, the `posts` array gets a
        # new item.
        # However, there is no permanent storage for this array. We
        # say that it is stored "in memory" only, and when the
        # server stops that memory data is unoaded. When you start
        # the python script again, the `posts` variable is reinitialized
        # to an empty array.
        #
        # If we wanted to have the posts live on between server
        # restarts, we would need some sort of permanent storage for
        # them. One way to do this would be to write out lines to a text
        # file every time a new post is added, and read that text file
        # when our flask app starts.
        #
        # Another option is to use a database such as MySQL, Postgresql,
        # MongoDB or another one. This is essentially the same
        # as saving it to a file on disk, but the databases use much
        # more sophisticated mechanisms for adding and reading data.

        posts.append({'name': name, 'text': text})
    return render_template('teacher.html', all_posts=posts)

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
