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
