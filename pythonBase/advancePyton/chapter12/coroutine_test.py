# 为什么需要使用协成？？？
# 1.回调模式编码复杂度高
# 2.同步编程的并发性不高
# 3.多线程需要现场同步
# 1.使用同步方式去编写异步代码
# 2.使用单线程去切换任务
#     2.1:线程是由操作系统切换的、单线程切换意味着我们需要程序员自己去调度
#     2.2:不在需要锁、并发性高、如果单线程内切换函数、性能远高于线程切换，并发性更高

# 我们需要一个可以暂停的函数、并且可以在适当的时候恢复该函数继续执行
# 出现协成-->有多个入口的函数，可以暂停的函数(可以向暂停的地方传入值)


def gen_fun():
    # 1，可以产出值
    # 2.可以产生值

    html = yield "http://www.baidu.coml"
    print(html)
    yield 1
    yield 2
    yield 3
    return "Aige"


if __name__ == '__main__':
    gen = gen_fun()
    # 启动生成器的方法有两种
    # 1. next
    # 2.send
    # 在滴啊用send发送非None之前，必须启动一起发送None值
    gen.send(None)
    html = 'bobby'
    print(gen.send(html))  # send可以将值出入生成器内部TypeError: can't send non-None value to a just-started generator
    print(next(gen))
    print(next(gen))
    # print(next(gen))
    # print(next(gen))
