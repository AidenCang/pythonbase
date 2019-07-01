import time
import threading

detail_url_list = []


# 共享变量不建议是用，变量的控制比较复杂

def get_detail_html(detail_url_list):
    while True:
        # 多线程判断变量会出现很多问题，例如if判断和pop的获取可能不在同一时间段内完成，出现多次获取抛异常的问题
        if len(detail_url_list) > 0:
            url = detail_url_list.pop()
            print("开始获取{} detail html".format(url))
            time.sleep(2)
            print("{} html 获取结束".format(url))


def get_detail_url(detail_url_list):
    print("开始获取{} detail url")
    time.sleep(2)
    for i in range(20):
        detail_url_list.append("http://projectedu.com/{id}".format(id=i))
    print("{} url 获取结束")


# 线程间通信方式--共享变量
if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    thread1.start()
    for i in range(20):
        thread2 = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        thread2.start()
