"""
# Milan Markovic
# 12/3/24

# The script sets up an HTTP server on localhost:9876.
# When a GET request is made, the server:

#     Responds with a 200 OK status.
#     Sends headers indicating the content is HTML.
#     Returns a simple HTML message: "Hello, this is your HTTP server!".

# The serve_forever method ensures the server continuously listens for and handles requests.
"""

# Set up an http server that listens on localhost:9876
# To check the server, run this script and go to http://localhost:9876 in your browser.
# To stop the server, press Ctrl+C in the terminal where the script is running (also closing the terminal where it's running should work).

from http.server import HTTPServer, BaseHTTPRequestHandler

# Inherits from BaseHTTPRequestHandler (this is how Python does inheritance)
# SimpleHTTPRequestHandler is a subclass of the superclass BaseHTTPRequestHandler
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    # This method is called whenever the server receives a GET request
    # It's a method of the BaseHTTPRequestHandler class, which we override here with our own implementation
    # (don't get confused, Python docs say do_GET() is part of the SimpleHTTPRequestHandler class, but it's actually inherited from BaseHTTPRequestHandler)
    def do_GET(self):
        # Basic response to any GET request
        self.send_response(200)
        self.send_header('Content-Type', 'text/hmtl')
        self.end_headers()
        self.wfile.write(b'Hello, this is your HTTP server!')

# This if statement ensures that the code below only runs if this file is run directly (and not as an imported or inherited class)
# Does not correspond to file name (eg, main.py), but to the name of the module (eg, __main__)
# That's Python's way of doing it
if __name__ == '__main__':
    # Set up the server
    server_address = ('', 9876)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Serving on localhost:9876')
    httpd.serve_forever()

