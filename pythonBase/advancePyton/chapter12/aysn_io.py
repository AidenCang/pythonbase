# 并发是指在同一时间段内，在同一个cpu上执行的的程序
# 并行是指任意时间点，有多个程序同时运行在多个cpu上
# 阻塞是不耗CPU
# 不停的询问连接是否建立好，需要while不断的循环查看状态

# io多路复用
# C10K问题
# 1999年提出来的技术挑战
# 1GHZ cpu、2Gn内存、1gbps网络环境下，单台服务器为1万用户提供服务的机制
# C10M  8核心CPU、64G内存、在10Gbps的网络上保持1000万并发连接


# select、pool、epoll都是I/O多路复用技术，本质上都是同步I/O
# 1.select可以同时监听多个socket连接，如果有数据里面可以解析准备好的Socket
# 2.Pool
# 3.epoll

# epoll并比一定是比select
# 在高并发的请求下，连接并不活跃，epoll比select效率更高
# 并发不高，同时连接活跃的请求下，select比epoll好


# Unix下的五种IO模型
# 1.阻塞IO
# 2.非阻塞IO
# 3.I/O复用
# 4.信号驱动IO
# 5.异步I/O（POSIX的aio_系列函数）

# select + 回调+事件循环



from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE
from urllib.parse import urlparse

import socket

selector = DefaultSelector()


class Fetcher:

    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode('utf8'))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)

        self.data.decode('utf8')
        # html_data = self.data.split("\r\n\r\n")[1]
        print(self.data.decode('utf8'))
        self.client.close()

    def get_url(self, url):
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass
        # 注册到Select中去
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


def loop():
    # 1.select 本身并不支持register模式
    # 2.socket状态变化以后的回调是由程序员处理
    while True:
        ready = selector.select()
        for key, mask in ready:
            cal_back = key.data
            cal_back(key)


if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()
