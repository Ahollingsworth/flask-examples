## Static files

Imagine what is happening when you run your application.
Where is the image of the football players coming from?
Answer: Your app is serving up both the index.html file
*and* the image of the football players.

But there is only one route in the app. How does it also
know to serve up the football image at the route "/static/football.jpg"?

Answer: This is a feature of Flask, and of most web servers, that it
can simply serve up a file directly off the disk to the web browser.
What kinds of files might this be used for? Answer: javascript assets,
css files, and images.

What happens if you change the 'url_for' part of the index.html to
reference a different filename, or a different folder name? Does it
still work? Can you figure out how to make it display the picture of an
island instead?
