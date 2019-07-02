# Python 基础

[Python基础开发Python Cookbook](https://python3-cookbook.readthedocs.io/zh_CN/latest/copyright.html)

[AdvancePython_resource](https://github.com/liyaopinner/AdvancePython_resource)

[advanced-java](https://github.com/doocs/advanced-java)

[Android-AdvancedWebView](https://github.com/delight-im/Android-AdvancedWebView)

[android-advancedrecyclerview](https://github.com/h6ah4i/android-advancedrecyclerview)

[Python-docs](https://docs.python-guide.org/)

编译语言：c、C++
解释型语言:Python,javascript

Python调用C、C++

Python：语言、风格

Python高性能与优化

常见的数据结构

Python深拷贝
partial 怎么使用
__weakref__
# request->urllib->socket

Python进价：
1.跟大神一起学习
2.阅读源码，懂原理
3.多做项目

python代码背后的设计原理

对生成器和迭代器的原理

Python异常处理

面向对象、魔法方法、元类、生成器、多线程、协程

一切皆对象:type/object/class
type的使用:

    1.生成一个类
    2.返回一个类型

object所有类的父类

    
魔法方法

    python数据模型
    数据模型对python的影响
    
python类

    多态
    抽象基类abc(不能实例化)
    MRO:属性查找算法C3算法
    DFS:深度优先查找算法-->Python2.3开始使用广度优先--->C3算法
    打印继承属性查找方法:A.__mro__
    __birthday  == _classname__birthday__可以调用
    自省，是通过一定的查询机制来查看对象内部结构，__dict__查看属性，dir也可以列出属性，没有属性值
    为什么要调用父类的方法
    super到底执行的顺序是什么

mixin:

    1.mixin类功能单一
    2.不和基类关联
    3.在mixin中不要使用super这种用法

上下文管理器with，Python是以协议规范来做的

    class Sample:

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__enter__")

    def do_something(self):
        print("do_something")

    if __name__ == '__main__':
        with Sample() as sample:
            sample.do_something()
            
    contextlib简化上下文管理器
        
        import contextlib
    
    
    @contextlib.contextmanager
    def open_file(file):
        print('open')
        yield {}  # 生成器的使用
        print('close')
    
    
    with open_file("textcontextlib") as file:
        print("操作文件")


    
Python序列化
深入dict和set

    dict的查找性能远远高于list，dict不会随着元素的数据增大而增大
    list随着数据量的增大、查询效率越低
    
迭代器和生成器

对象引用和可变性、垃圾回收
元类编程
socket

多进程和多线程
异步io和协程
asyncio并发编程
对象自省机制
上下文管理器
contextlib实现上下文管理器
property动态属性
__getattr__,__getattribute__区别
属性描述符
__new__和init的区别
元类实现ORM


多线程、多进程
多线程、多进程通信
多线程、多进程使用场景和比较？
多线程、多进程线程安全使用
多线程、多进程同步
线程池的使用

GIL和多线程
线程通信--共享变量、Queue
线程同步锁-Lock、RLock、Condition、semaphores
线程池原理分析-ThreadPoolExecutor
多进程编程、多进程通信
IO多路复用-select、poll、epool
select+回调+事件循环模式
生成器进价-send、close、throw和yield from
async和await两个关键词的作用
Feature和Task
aiohttp实现高并发抓取url
asyncio背后的selector
协程同步和通信
ThreadPoolexecutor+asyncio结合使用



# pythonbase
