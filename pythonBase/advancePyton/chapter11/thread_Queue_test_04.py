import time
import threading
from queue import Queue

detail_url_list = []


# 共享变量不建议是用，变量的控制比较复杂
# 队列的使用PriorityQueue/LifoQueue
# 自己实现队列，deque队列的实现
# from collections import deque,defaultdict
# https://www.cnblogs.com/zhenwei66/p/6598996.html

def get_detail_html(detail_queue):
    while True:
        # 多线程判断变量会出现很多问题，例如if判断和pop的获取可能不在同一时间段内完成，出现多次获取抛异常的问题
        url = detail_queue.get()
        print("开始获取{} detail html".format(url))
        time.sleep(2)
        print("{} html 获取结束".format(url))


def get_detail_url(detail_queue):
    print("开始获取{} detail url")
    time.sleep(2)
    for i in range(20):
        detail_queue.put("http://projectedu.com/{id}".format(id=i))
    print("{} url 获取结束")


# 线程间通信方式--共享变量
if __name__ == '__main__':
    detail_queue = Queue(maxsize=1000)
    # detail_queue.join()
    # detail_queue.task_done()
    # detail_queue.get()
    # detail_queue.put()
    # detail_queue.put_nowait()
    # detail_queue.get_nowait()
    # detail_queue.empty()
    detail_queue.full()

    thread1 = threading.Thread(target=get_detail_url, args=(detail_queue,))
    thread1.start()
    for i in range(20):
        thread2 = threading.Thread(target=get_detail_html, args=(detail_queue,))
        thread2.start()
