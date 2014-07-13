## Templates v2.0

What is different about the index page now?

How does it show the name Robot? You don't see the word Robot in the
index.html, do you? Why not? How did the word get there?

### Experiments

  * Change the index page so that is shows Your name
  * Change the index page so that it says your name and your age.
    But do it without putting your age directly in the index.html.
  * What happens if you put a variable in your template that you do
    not mention in your 'render_template' method call?

### Teacher Guide

This example shows how to use the 'interpolation' features of the
jinja2 templating system. It is possible to add multiple keyword
arguments to the `render_template` method (after the first argument,
which names the template), and inside the template the jinja2
templating system will replace variable names inside `{{` and `}}`
with the values that were passed in to the `render_template` method.

For example, if the template includes the text `{{ name }}`, and
the `render_template` method includes a keyword argument `name='Robot'`,
then the HTML that Flask sends to the browser will replace that
section of the template with the string 'Robot'.

Jinja2 also allows the execution of code (loops, for example), by
putting the code within `{%` and `%}` identifiers. We'll touch on
this in later lessons.
