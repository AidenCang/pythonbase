import threading
from threading import Lock, RLock

# python线程加锁Lock、Rlock
# 获取锁和释放锁都需要时间，影响性能
# 锁会引起死锁
# 长时间使用锁，不释放
# 调用的次数要相等:lock.acquire()lock.release()
# Rlock可从入锁，在同一个线程中可以多次调用acquire、release

total = 0
lock = Lock()

def add(lock):
    global total
    for i in range(1000000):
        lock.acquire()
        total += 1
        lock.release()


def desc(lock):
    global total
    for i in range(1000000):
        lock.acquire()
        total -= 1
        lock.release()


thread1 = threading.Thread(target=add, args=(lock,))
thread2 = threading.Thread(target=desc, args=(lock,))
thread1.start()
thread2.start()
thread1.join()
thread2.join()

print(total)
