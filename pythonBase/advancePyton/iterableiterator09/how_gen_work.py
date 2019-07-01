# python中的函数允许原理
# python.exe会调用pyEval_EvalframEx(c函数)去执行foo函数，首先会创建一个栈帧
# python一切皆对象、栈帧对象、字节码对象
# 当foo调用函数bar，又会创建一个栈帧
# 所有的栈帧都是分配在堆内存之上、这就决定了栈帧独立于调用者而存在

# 生成器实现是利用函数调用代码是在栈中执行的特性来实现的
# 生成器可以控制函数的运行和暂停


def foo():
    pass


def bar():
    pass


import dis

print(dis.dis(foo()))
