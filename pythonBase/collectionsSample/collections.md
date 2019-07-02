# Python web 和 Python爬虫
# 集合和队列的关系
deque是通过GIL是线程安全的，list不是线程安全的
tuple的功能

    1.不可变、可迭代
    2.拆包
    3.tuple不可变现不是绝对的
    4.tuple和list比较
    immutable:
    1.性能优化
    2.线程安全
    3.可以作为dict的key(可哈希的对象才能作为dict的key)
    4.拆包特性
    用C语言来做对比：
    1.tuple相当于struct
    2.list相当于数组
    
    
namedtuple
defaultdict
deque
counter
OrderedDict
ChainMap