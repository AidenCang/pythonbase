# Python中的垃圾回收机制的算法是采用，引用计数
a = 1
b = 2
del a  # 调用类中的del方法


class A:
    def __del__(self):
        pass
