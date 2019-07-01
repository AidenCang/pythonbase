# 控制类实例化的过程
from datetime import datetime, date
import numbers


# def __getattr__(self, item): 在属性获取不到的时候调用
# def __getattribute__(self, item):  调用熟悉是首先调用，不建议重写
# 属性描述符和属性的查找过程


class IntField(object):  # 属性描述符
    def __set__(self, instance, value):
        if isinstance(value, numbers.Integral):
            self.value = value
        else:
            error = '{} is not number '.format(value)
            raise ValueError(error)

    def __get__(self, instance, owner):
        return self.value

    def __del__(self):
        pass


class UserModel:
    age = IntField()




class User:

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = date(year=1991, month=3, day=28)
        self._age = 0

    def get_age(self):
        return datetime.now().year - self.birthday.year

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value

    def __getattr__(self, item):
        return "{} not find ".format(item)

    # def __getattribute__(self, item):
    #     # 对象调用时会首先调用
    #     return "Aige"


if __name__ == '__main__':
    user = User('cck', 'a')
    print(user.birthday)
    # print(user.get_age())
    print(user.age)
    print(user.name1)

    usermodel = UserModel()
    usermodel.age = 28
