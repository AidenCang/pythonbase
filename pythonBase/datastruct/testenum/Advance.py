from enum import Enum, unique


# 枚举定义
# 枚举迭代
# 枚举比较


@unique
class VIP(Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOUR = 4
    FIVE = 5


print(VIP.FIRST)

for v in VIP.__members__.items():
    print(v)

print(type(v))  # 枚举在python中是元组类型
