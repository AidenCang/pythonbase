# 文件读写、数据库读写分离，通常一个线程写，多个线程读
# 控制进入数量的类
import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            print()
            html_thread = HtmlSpider("https://baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    urlproducer = UrlProducer(sem)
    urlproducer.start()
