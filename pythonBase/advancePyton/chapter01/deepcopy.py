# _*_ encoding:utf8 _*_
import copy

a = [1, 2, 3, 4, ['a', 'b', 'c']]

b = copy.copy(a)

c = copy.deepcopy(a)


print(b)
print(c)
