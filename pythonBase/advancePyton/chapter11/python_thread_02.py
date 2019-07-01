import time
import threading


# 线程实现的两种方式
# 1.方法方式实现
# 2.以继承方式实现


class GetDetailHtml(threading.Thread):
    def __init__(self, name):
        super(GetDetailHtml, self).__init__(name=name)

    def run(self):
        print("开始获取{} detail html")
        time.sleep(2)
        print("{} html 获取结束")


class GetDetailURL(threading.Thread):
    def __init__(self, name):
        super(GetDetailURL, self).__init__(name=name)

    def run(self):
        print("开始获取{} detail url")
        time.sleep(2)
        print("{} url 获取结束")


if __name__ == '__main__':
    thread1 = GetDetailHtml('GET Detail Html')
    thread2 = GetDetailURL()

    thread1.start()
    thread2.start()
