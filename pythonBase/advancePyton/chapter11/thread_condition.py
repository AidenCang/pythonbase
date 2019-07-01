import threading
from threading import Lock, RLock

# lock = Lock()
lock = threading.Condition()


# Condition有两层锁，一把是内部自己使用，你能一把是其他调用了wait()使用的锁，使用双端队列来保存锁

class XiaoAi(threading.Thread):
    def __init__(self, lock):
        super().__init__(name="小爱同学")
        self.lock = lock

    def run(self):
        with self.lock:
            print("{} : 天猫".format(self.name))
            self.lock.notify()
            self.lock.wait()

            print("{} : 今天天气怎么样".format(self.name))
            self.lock.notify()
            self.lock.wait()


class TianMao(threading.Thread):
    def __init__(self, lock):
        super().__init__(name="天猫精灵")
        self.lock = lock

    def run(self):
        with self.lock:
            self.lock.notify()
            self.lock.wait()
            print("{} : 在".format(self.name))

            self.lock.notify()
            self.lock.wait()
            print("{} : 今天天气非常好".format(self.name))


if __name__ == '__main__':
    tianmao = TianMao(lock)
    xiaoai = XiaoAi(lock)

    tianmao.start()
    xiaoai.start()
    tianmao.join()
    xiaoai.join()
