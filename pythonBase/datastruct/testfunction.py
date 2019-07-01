# 函数
# 1.功能性
# 2.隐藏细节
# 3.避免实现重复的代码
# 4.组织代码

# inspect 一个Python内置的标准库
# drill 是一个第三方库

# 参数：
# 1.必要参数
# 2.关键字参数
# 3.默认参数
# 4.可变参数

# 设置递归层数
import sys

sys.setrecursionlimit(100000)


def add(x, y):  # 没有return的语句返回的是None
    print(x + y)


print(add(3, 5))
print(add)

a, b, _ = [1, 2, 3, 4, 5, 6, 7, 8]
print(a, b, _)
