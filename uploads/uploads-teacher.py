from flask import Flask, request, render_template
import os
# We have another new import this time: "os"
# "os" is a python library that provides a number of
# methods to interact with the operating system such
# as reading and writing files.

app = Flask(__name__)

@app.route('/teacher', methods=['GET', 'POST'])
def upload_file():
    # The path to the image is "~/uploads/static/image.jpg",
    # which will be the user's home directory + "/uploads/static",
    # which means that when run on nitrous the static
    # directory will be the one inside the "uploads" directory for
    # this example.
    image_path = os.path.expanduser(
            os.path.join("~","uploads","static","image.jpg"))

    # If this route was requested via POST then it must have come
    # from the form, so read in the POSTed file and save it to
    # the image_path. If the image_path already exists, this will
    # overwrite it with a new image.
    if request.method == 'POST':
        file = request.files['file']
        file.save(image_path)

    # If the operating system tells us that an image file exists at
    # the page, then we will show that in the template.
    has_file = os.path.exists(image_path)
    return render_template('teacher.html', show_image=has_file)

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
