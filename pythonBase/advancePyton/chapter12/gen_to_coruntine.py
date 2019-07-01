# 生成器是一个可以暂停的函数
import inspect


def gen_fun():
    yield 1
    return "bobby"


if __name__ == '__main__':
    gen = gen_fun()
    print(inspect.getgeneratorstate(gen))
    next(gen)
    print(inspect.getgeneratorstate(gen))
    try:
        next(gen)
    except StopIteration as e:
        pass
    print(inspect.getgeneratorstate(gen))
