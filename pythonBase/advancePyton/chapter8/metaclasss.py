# 类本身是对象，type创建类
# 元类，是创建类的类
# python类实例化过程，会首先寻找metaclass,通过metaclass去创建user类，
# 父类没有回一直向上找metaclass，模块中查找，知道找不到才会调用类的过程
# 抽象ABCMeta类的实现过程

class MetaClass(type):  # 控制类实例化的过程
    def __new__(cls, *args, **kwargs):
        return super(MetaClass, cls).__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):  # 类的实例化过程
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


if __name__ == '__main__':
    user = User("aige")
    print(user.__str__())
