import socket, time

SERVER_IP = '192.168.0.11'
SERVER_PORT = 10940

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (SERVER_IP, SERVER_PORT)

print(f'Trying to connect to {server_address}')
sock.connect(server_address)
message = b'\x02000EAR01B19B\x03'
sock.send(message)
print(f"Sent: {message}")
time.sleep(0.1)
try:
    while True:
        response = sock.recv(1024)
        if response:
            print(f"Received: {response}")
        else:
            print('No more data')
            break
finally:
    sock.close()
