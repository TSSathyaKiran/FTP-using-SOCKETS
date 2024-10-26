import socket

# use same port
# and address

PORT = 5001
ADDR = '127.0.0.1'
file_name = "luffy.jpg"

# socket.AF_INET is because im using TCP
# socket.SOCK_STREAM is to initialize TCP

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ADDR, PORT))
server.listen()
print("Connect CLIENT to HOST: {ADDR} and PORT: {PORT}")

client, addr = server.accept()
print(f"Connected to {addr}")

# we shall encode the file_name before sending it
# coz why not

client.send(file_name.encode('utf-8'))

# no loop used here to send the data
# we can also encode the data and decode it later on client for security

with open(file_name, 'rb') as file:
    data = file.read()
    client.sendall(data)
print("Sent file")


file.close()
client.close()
server.close()