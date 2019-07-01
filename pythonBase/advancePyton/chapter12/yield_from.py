# python 3.3yield from


from itertools import chain

my_list = [1, 2, 3]
my_dict = {
    "bobby1": "http://projectedu.com",
    "bobby2": "http://www.imooc.com"
}


def my_chain(*args, **kwargs):
    for my_iterable in args:
        # for value in my_iterable:
        #     yield value
        yield from my_iterable


#
# for value in chain(my_dict, my_list, range(5, 10)):
#     print(value)
#
# for value in chain(my_dict, my_list, range(5, 10)):
#     print(value)


def g1(gen):
    yield from gen


# 1.main调动g1(委托生成器),gen子生成器
# 2.yield from会在调用子生成器之间建立一个双向通道
def main():
    g = g1()
    g.send(None)
