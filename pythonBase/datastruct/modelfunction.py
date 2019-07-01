# 包、模块、类
import sys

from pythonBase.datastruct.BaseStruct import a

import io

# 模块内置变量
dir = dir()  # 显示当前的模块下的变量
print(dir)

# 入口函数中是不能使用相对路劲，入口函数模块会被强制添加__main__.package
# 使用 python -m datastruct.pakcage 可以强制改变包的路径

# ['__annotations__', '__builtins__', '__cached__',
# '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__']
# python 之禅 import this
print(__name__)
print(__package__)
print(__file__)
print(__doc__)
