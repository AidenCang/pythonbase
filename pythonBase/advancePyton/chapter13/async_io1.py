# 包括各特定系统实现的模块化时间循环
# 传输和协议抽象
# 对TCP、UDP、SSL、子进程、延时调用以及其他具体支持

# 模仿futures模块但使用于事件循环使用的Futures类

# 基于yiel from的协议和任务，可以支持顺序的方式编写并发代码
# 必须使用一个将产生阻塞I/O的调用时，有接口可以把这个事件转移到线程池
# 模仿threading模块中的同步原语、可以用在单线程的协程之间

# 事件+循环(驱动生成器)+epoll(IO多路复用)
# asyncio是python用于解决异步io编程的一整套解决方案
# tornado、gevent、twisted(scrapy,django channels)
# tornado(实现了服务器)，django+flash(uwsgi,gunicorn+nginx)
# tornado可以直接部署

# wait和gather使用和区别
# wait和gather区别
# 1.gather更加高层的功能分装

# 使用asyncio
import time
import asyncio


# import asynchat
# import asyncore

async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(get_html("http://www.imooc.com"))
    tasks = [get_html("http://www.imocc.com") for i in range(10)]
    asyncio.create_task()
    loop.run_until_complete(asyncio.wait(tasks))
    print(time.time() - start_time)
