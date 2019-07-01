# 业务逻辑开发者，不考虑封装性
# 包、类库的开发者

# 函数式编程
# 闭包 = 函数+环境变量
# 命令式编程、函数式编程
# Python支持函数式编程、并不是函数式编程


def cave_pre():
    a = 25

    def cave(x):
        return a * x * x

    return cave


f = cave_pre()

print(f)
print(f.__closure__[0].cell_contents)
print(f(2))

origin = 0


def factory(pos):
    def go(step):
        nonlocal pos  # 记录上次调用的环境
        new_pos = pos + step
        pos = new_pos
        return pos

    return go


tourist = factory(origin)
print(tourist(2))
print(tourist(3))
print(tourist(4))
