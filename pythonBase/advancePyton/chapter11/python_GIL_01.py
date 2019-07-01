# GIL全局终端锁 global interpreter Lock(cpython)
# python中的一个线程对应c语言中的一个线程
# GIL是的python同一时间只能有一个线程运行的cpu上执行字节码
# gil会根据执行的字节码行数以及时间片切换线程(时间片的时间)，无法将多个线程映射到多个CPU上,gil遇到IO操作的情况下主动释放

# 对io操作来说，多线程和多进程效率差不多
# 共享变量和Queue
# pipy去GIL化的库
# Gil会根据执行的字节码行数以及时间片释放GIL，遇到IO操作的时候回释放GIL

# GIL在python2，Python3中的区别

# Python和Cpython的区别
# +=============dis查看字节码===================
# import dis
#
#
# def add(a):
#     a = a + 1
#     return a
#
#
# print(dis.dis(add))
# +=============dis查看字节码===================
total = 0


def add():
    global total
    for i in range(1000000):
        total += 1


def des():
    global total
    for i in range(1000000):
        total -= 1


import threading

thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=des)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print(total)
