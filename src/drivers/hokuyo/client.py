import socket, sys

SERVER_IP = 'localhost' if sys.argv[1] == 'test' else '192.168.0.10'
SERVER_PORT = 10940

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (SERVER_IP, SERVER_PORT)

print(f'Trying to connect to {server_address}')
sock.connect(server_address)
