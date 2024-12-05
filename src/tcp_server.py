"""
# This code sets up a custom TCP server to:

#     Listen on localhost:9876.
#     Accept incoming client connections.
#     Read and parse client requests.
#     Send back a basic HTTP-like response.
#     Close the connection once the response is sent.

# The difference with a TCP server from an HTTP server is with a TCP server, 
# you need to manually handle details like parsing requests and formatting responses.
# TCP servers also aren't friendly with web browsers, like HTTP servers are.
# You would run the TCP server in the terminal, then use a tool like telnet to connect to it.
"""

# Set up tcp server that parses incoming requests and sends back a response.

import socket

HOST = '127.0.0.1'
PORT = 9876

# clinet_socket represents a connection to the client
def handle_client(client_socket):
    request = client_socket.recv(1024).decode('utf-8')  # Receive data (request) from the client
    print(f"Received request:\n{request}")  # typically shows the HTTP like request sent by the client

    # response that will be sent back to the client
    response = (
        'HTTP/1.1 200 OK\n'
        'Content-Type: text/html\n\n'
        "Hello, you've connected to the TCP server!"
    )

    # actually sends the response to the client
    client_socket.sendall(response.encode('utf-8'))
    client_socket.close()

if __name__ == '__main__':
    # Create a new TCP socket object
    # socket.AF_INET: specifies the IPv4 address family
    # socket.SOCK_STREAM: specifies a TCP connection (as opposed to a UDP connection)
    # with block: ensures the socket is automatically closed when the block is exited
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind((HOST, PORT))
        server.listen(5)
        print(f"Serving on {HOST}{PORT}")
        while True:
            client_socket, client_addr = server.accept()    # waits for a client to connect (eg, for someone to go to the http link). server.accept() returns a tuple of 2 items: the client socket (a new socket for communication with the connected client) and the client address (IP and port)
            print(f"Connection from {client_addr}")     # logs address of connected client
            handle_client(client_socket)    # calls the handle_client function to handle the client's request
