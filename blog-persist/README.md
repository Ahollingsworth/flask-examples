## Blog Persisted

This is a continuation of the "blog" app that saves new blog posts to a
file. The original "blog" app will lose all its posts whenever the
server is stopped and restarted, but this version saves the posts to
a file called "posts.txt", so it can be restarted later.

This is essentially what a database does, although a db is highly
optimized to allow very fast saving (writing the file to disk) and
reading/searching.

## Experiments

  * How would you add the date along with each post automatically?
  * Make a few posts and then inspect the posts.txt file. How does the
    text there correspond to what you posted? What extra info is there?
  * What happens if you delete a line from the posts.txt file?
  * Come up with a new way to encode the text to save to disk. You'll
    have to change both how `write_post` works and how `read_posts`
    works.
  * The text is encoded using a special two-character string "::". What
    happens if you use this same special string in the form in the
    browser as part of your name or the text? Why does this break the blog?
  * The couple lines of code that are used to find the path of the file
    are used in two places -- how could you use a function to do that
    work instead?

### Teacher guide

The blog-persist-teacher.py file has lots of comments explaining what is
happening.
