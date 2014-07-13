## Micro Blog

This is a full-featured app that lets you and your friends create a
blog.

How does the blog store its posts? What happens if you stop the python
server and start it again? Where did the posts go? Why do they not
stay?

This index.html template has something we haven't seen before:
`{% for %}`. What does that do?

## Experiments

  * How would you add the date along with each post automatically?

### Teacher guide

We introduce some more conditional logic (loops) in the template this
time. Similar to how we can loop through a list in the python
interactive prompt, we can loop through a list in a jinja2 template.

The `{% for post in all_posts %}` text in the template will repeat
the inner part once for each item in the `all_posts` array, using
the variable name `post` for each one.
