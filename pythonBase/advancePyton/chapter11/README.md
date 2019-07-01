# GIL全局终端锁 global interpreter Lock(cpython)
# python中的一个线程对应c语言中的一个线程
# GIL是的python同一时间只能有一个线程运行的cpu上执行字节码
# gil会根据执行的字节码行数以及时间片切换线程(时间片的时间)，无法将多个线程映射到多个CPU上,gil遇到IO操作的情况下主动释放

# 对io操作来说，多线程和多进程效率差不多
# 共享变量和Queue

#生成器使用for循环来做的

Lock/Rlock/Condition/semphere/Event

#/Users/cangck/Library/Caches/PyCharm2019.1/python_stubs/-1845636981/_collections.py

    defaultdict
    deque
    OrderedDict
    _deque_iterator
    _deque_reverse_iterator
    __loader__