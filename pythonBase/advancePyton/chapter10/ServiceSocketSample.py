import socket
import threading
from functools import partial, lru_cache

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 8001))
server.listen()


def handle_connect_socket(sock, addr):
    # 获取从客户端发送的数据
    # 一次获取1k的数据
    size = 1024
    while True:
        data = sock.recv(size)
        recevi = data.decode("utf8")
        if recevi == "end":
            break
        print(recevi)
        rest = input()
        sock.send(rest.encode("utf8"))


while True:
    sock, addr = server.accept()
    client_thread = threading.Thread(target=handle_connect_socket, args=(sock, addr))
    client_thread.start()

server.close()
sock.close()
