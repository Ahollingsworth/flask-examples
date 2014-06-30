from flask import Flask, request, render_template
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    image_path = os.path.expanduser(
            os.path.join("~","uploads","static","image.jpg"))

    if request.method == 'POST':
        file = request.files['file']
        file.save(image_path)

    has_file = os.path.exists(image_path)
    return render_template('index.html', show_image=has_file)

if __name__ == "__main__":
    print("To view your site, click the 'preview' menu and choose port 3000")
    print("To stop your app and return to the command line, type control-C")
    app.run(host='0.0.0.0', port=3000, debug=True)
