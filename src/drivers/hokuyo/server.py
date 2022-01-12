import socket, sys

SERVER_IP = '0.0.0.0'
SERVER_PORT = 10940

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (SERVER_IP, SERVER_PORT)

print(f'Starting server on {server_address}')
sock.bind(server_address)

sock.listen()

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            try:
                data = connection.recv(100)
                print('received "%s"' % data)
            except:
                data = None
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print('no more data from', client_address)
                break
            
    finally:
        # Clean up the connection
        connection.close()