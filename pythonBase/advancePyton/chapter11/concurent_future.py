from concurrent.futures import ThreadPoolExecutor, as_completed, wait, FIRST_COMPLETED
from concurrent.futures import Future  # task返回容器

# futures是对多线程和多进程进行开发的包
# 线程池、为什么要线程池
# 主线程中获取摸个线程的状态或一个任务的状态，以及返回值
# 当一个线程完成是主线程立马知道
# future可以让多线程和多进程编码接口一致
# task1.done()
# task1.result()
# task1.cancel()
# task1.
# wait()函数的使用


import time


def get_html(times):
    time.sleep(times)
    print("get page {}".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
task1 = executor.submit(get_html, 3)
task2 = executor.submit(get_html, 2)

print(task1.done())
time.sleep(3)
print(task1.done())
print(task1.result())

# 获取已完成的task任务、as_completed()
urls = [3, 2, 4]
all_task = [executor.submit(get_html, (url)) for url in urls]
for futurereslt in as_completed(all_task):
    data = futurereslt.result()
    print("get {}  page result".format(data))
wait(task1, return_when=FIRST_COMPLETED)
print("FIRST_COMPLETED")
from concurrent import futures

# 通过executor获取已完成的task
for data in executor.map(get_html, (urls)):
    print("get {} page result ".format(data))
