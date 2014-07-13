## Uploads

There's a form on the index.html template again this time, but
there is something different about it. What's different about the form?
Answer: It has an "enctype", which is a way of telling the server that
you'll be uploading a file.

### Experiments

  * The same route ("/") handles two HTTP verbs. What are they? (GET and
    POST)
  * How does the route behave when it is a GET request?
  * How does the route behave when it is a POST request?
  * Where does the uploaded file go?
  * What happens if you upload one file, and then another. Is the
    original file still around? Why or why not?

### Teacher guide

Similar to the "forms" example, this flask app has a route that can
be reached via GET or POST.

In this case, though, the route only receives form data via POST.
If the browser requests it via GET, then it shows the teacher.html
template. If the route is requested via POST, then it reads in
a file and saves it to the path "~/uploads/static/image.jpg".

The "~" in unix expands to the user's home directory, so this
ensures that the uploaded image gets saved to the "uploads/static/"
directory with a name of "image.jpg". There is a caveat here: the
uploaded image must be of type jpg since we are saving it as
"image.jpg". If the file is a ".png" or ".gif" and we save it as
"image.jpg", then the browser may interpret it incorrectly and not
be able to display it.
