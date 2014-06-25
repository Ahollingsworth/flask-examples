## Templates

View the app.py file. What is different about this one compared to your
routes/app.py file? What is different about the first line?

Answer: In the previous app.py file, we imported 'Flask'. This time we
are importing *two* things from 'flask'. What is the other one? What is
it used for?

Answer: It is the render_template method. What do you think that is used
for?

### Experiments

  * The file just says "render_template('index.html')". Where is
    index.html? Can you change it so that it prints out your name on the
    page?
  * Change this app so that the page has a title of your choosing.
  * What happens if you remove the "return" word on line 6 of app.py?
    What do you think is happening?
    Look at the command line after you load your page now. What is
    different? (Answer: 500 status code). What does the 500 mean?
  * add back the "return" keyword.
  * Make another route ("/about")
  * Change your index page so that it has a link to the about page.
  * Make the about page have a link to the index page.
