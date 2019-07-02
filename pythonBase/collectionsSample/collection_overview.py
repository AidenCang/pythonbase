import sys
from collections import namedtuple

# 判断系统版本号
if sys.version_info >= (3, 6):
    print(sys.version_info)
if sys.version_info >= (3, 5):
    print(sys.version_info)
# 处理数据库放回的数据，然后在添加一列
User = namedtuple('User', ['name', 'age', 'height', 'edu'])
# user = User(name='bobby', age='20', height=175)
user_tuple = ('bobby', 29, 175)
user = User(*user_tuple, 'master')
print(user.name, user.age, user.height)


# 函数参数
def ask(*args, **kwargs):
    print(args)
    print(**kwargs)


ask('aige', 20, {'key': 20})
