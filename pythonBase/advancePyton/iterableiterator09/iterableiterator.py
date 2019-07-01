from collections.abc import Iterable, Iterator


# 什么是迭代器和可迭代对象

class Company(object):
    def __init__(self, employee):
        self.employee = employee

    # def __iter__(self):
    # return 1  # TypeError: iter() returned non-iterator of type 'int'
    # pass

    def __getitem__(self, item):  # TypeError: 'Company' object is not iterable
        return self.employee[item]


class MyIterator(Iterator):

    def __init__(self, employee_list):
        self.employee_list = employee_list
        self.index = 0

    # def __next__(self):


if __name__ == '__main__':
    company = Company(['Aige', 'body', 'bob', 'tom'])
    for com in company:
        print(com)
