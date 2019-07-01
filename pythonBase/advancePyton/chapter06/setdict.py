# 深拷贝、浅拷贝
# 不建议继承list、dict
import copy
from collections import defaultdict, UserDict, UserList, UserString
from collections.abc import Mapping, MappingView, MutableMapping

# set集合fronzenset区别(不可变集合) 无序、不重复
# frozenset 可作为dict的key
new_set = set(['a', 'b', 'c'])
# new_set.update()
# new_set.difference()
# set性能很高


print(type(new_set))
a = {'a': 20, 'b': 15, 'c': 20}
print(a)
copy.deepcopy(a)
a['a'] = 50
print(a)

# dict.fromkeys()

print(a.get('b', default={}))
