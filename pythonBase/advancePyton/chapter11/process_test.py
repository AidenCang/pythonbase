# 多线程编程
# GIL锁在单cpu上只能执行一个，效率低
# 多进程可以在多个cpu上执行

# 多线程和多线程都能够并发为什么在IO操作是不使用多进程
# 进程切换比较耗时
# 1.对于耗cpu，多进程优于多线程
# 2.对于IO操作，多线程由于多进程

from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import os

import time

# pid = os.fork()  # 同时会存在两个进程，会拷贝父进程中的代码和数据到子进程中
#
# print("boby")
#
# if pid == 0:
#     print("子进程 {} , 父进程 {}.".format(os.getpid(), os.getppid()))
# else:
#     print("父进程 {}.".format(pid))

# 多进程
import multiprocessing


def get_html(n):
    time.sleep(n)
    return n


class MyProcess(multiprocessing.Process):
    def run(self):
        pass


if __name__ == '__main__':
    process = multiprocessing.Process(target=get_html, args=(2,))
    print(process.pid)
    process.start()
    process.join()
    print(process.pid)
    print("multiprocessing is end")

    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    # result = pool.apply_async(get_html, (2,))
    # pool.close()
    # print(result.get())

    for result in pool.imap(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))
