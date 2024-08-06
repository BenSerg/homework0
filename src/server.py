import socket

SERVER_IP = "127.0.0.1"
PORT = 5000

listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

listening_socket.bind((SERVER_IP, PORT))

listening_socket.listen()

print("Ожидание подключения...")
try:
    while True:
        socket_for_communication, addr = listening_socket.accept()
        print(f"Подключено ip={addr[0]}, port={addr[1]}")

        response = "ОК"
        socket_for_communication.sendall(response.encode("utf-8"))

        socket_for_communication.close()
except KeyboardInterrupt:
    print("Завершение работы сервера")