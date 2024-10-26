import socket

# using local host
ADDR = '127.0.0.1'
PORT = 5001

# socket.AF_INET is because im using TCP
# socket.SOCK_STREAM is to initialize TCP

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ADDR, PORT))
print("Connected")

# decodes the received file_name
file_name = client.recv(1024).decode('utf-8')

# this is important to not save with the same name,
# because if it recieved the same name this wouldnt work if both server and client was on the same device
# as this program saves the file in the same directory as the program itself hence with the sending file itself,
# that is, it would create the same file but get overrided because a file with the same name exists

file_name = f"Recieved_" + file_name

with open(file_name, 'wb') as f:

    # this loop it there so as to receive only 1024 bytes ata time
    # and the loop stops when file_data stops receiving any data

    while True:
        file_data = client.recv(1024)
        if not file_data:
            break

        f.write(file_data)

print("Received! ")
