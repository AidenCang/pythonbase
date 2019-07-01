# 生成器函数、只要函数里面有yield关键字就是生成器函数
def gen_func():  # 返回生成器对象，python编译成字节码是产生
    # 提供了惰性求值、延迟求值的可能
    yield 1


def fib(index):
    if index <= 2:
        return 1
    else:
        return fib(index - 1) + fib(index - 2)


if __name__ == '__main__':
    gen = gen_func()
    print(fib(10))
