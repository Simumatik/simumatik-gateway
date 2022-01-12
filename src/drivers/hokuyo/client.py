import socket, time

SERVER_IP = '192.168.0.9'
SERVER_PORT = 10940

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (SERVER_IP, SERVER_PORT)

print(f'Trying to connect to {server_address}')
sock.connect(server_address)
message = b"Hej"
sock.send(message)
print(f"Sent: {message}")
time.sleep(1)
response = sock.recv(1024)
print(f"Received: {response}")
sock.close()
