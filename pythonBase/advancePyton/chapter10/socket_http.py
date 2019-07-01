# request->urllib->socket
import socket
from urllib.parse import urlparse


def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = '/'

    # 建立socket连接
    clinet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clinet.connect((host, 80))

    clinet.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    data = b''
    while True:
        d = clinet.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode('utf8')
    # 去掉Http头部
    # data = data.split("\r\n\r\n")[1]
    print(data)
    clinet.close()


if __name__ == '__main__':
    get_url("https://www.baidu.com/")
