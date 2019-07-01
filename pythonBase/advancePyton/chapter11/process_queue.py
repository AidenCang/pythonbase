from multiprocessing import Process, Queue, Pipe, Manager
# 共享全局变量不适用于多进程编程
# import multiprocessing中不能用于Pool创建的进程池中的进程通信的
# Pipe()性能高于Manager
import time


# def producer(queue):
#     index = 0
#     while True:
#         index += 1
#         queue.put(index)
#         time.sleep(2)
#
#
# def consumer(queue):
#     while True:
#         data = queue.get()
#         print(data)


# if __name__ == '__main__':
#     queue = Queue(10)
#     producer = Process(target=producer, args=(queue,))
#     consumer = Process(target=consumer, args=(queue,))
#     producer.start()
#     consumer.start()
#     producer.join()
#     consumer.join()

# 使用Pip进程间通信
# def producer(pip):
#     index = 0
#     while True:
#         index += 1
#         pip.send(index)
#         time.sleep(2)
#
#
# def consumer(pip):
#     while True:
#         data = pip.recv()
#         print(data)
#
#
# # Manager通信方式
# if __name__ == '__main__':
#     pip_recv, pip_send = Pipe()
#     # Pipe只使用与两个进程间通信
#     producer = Process(target=producer, args=(pip_send,))
#     consumer = Process(target=consumer, args=(pip_recv,))
#     producer.start()
#     consumer.start()
#     producer.join()
#     consumer.join()


# 共享内存通信

def add(p_dict, key, value):
    p_dict[key] = value


if __name__ == '__main__':
    process_dict = Manager().dict()
    first_process = Process(target=add, args=(process_dict, "Aige1", 22))
    second_process = Process(target=add, args=(process_dict, "Aige2", 23))
    first_process.start()
    second_process.start()
    first_process.join()
    second_process.join()
    print(process_dict)
