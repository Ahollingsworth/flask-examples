## Routing

Your first app had one route. What was it? This app has two routes. What
are they?

### Experiments

  * Add a third route
  * Change the "about" route to print information about yourself.
  * When you visit a page while your server is running, what shows up
    on your command line. What does that message mean?

### Teacher notes

  * The server shows this on the command line:
  * `127.0.0.1 - - [13/Jul/2014 19:03:00] "GET / HTTP/1.1" 200 -`
  * This shows:
    * the IP address of the server (127.0.0.1)
    * the datetime
    * the HTTP verb ("GET")
    * the url ("/")
    * The HTTP method ("HTTP/1.1")
    * And the HTTP status code ("200" -- which means "success")
