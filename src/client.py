import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


client_socket.connect(("127.0.0.1", 5000))

client_socket.sendall(b"")

data = client_socket.recv(1024)
received_message = data.decode("utf-8")

print("Received:", repr(received_message))

if received_message == "ОК":
    print("Сообщение от сервера: ОК")

client_socket.close()