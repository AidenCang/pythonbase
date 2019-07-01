# Python和java中的变量是不一样的，python中的变量是一个指针
# is  判断是否为同一个对象
# == 表示值相等 __eq__

a = 'abc'
b = a
print(b is a)
print(id(b))
print(id(a))

print("=================")
c = [1, 2, 3, 4]
d = [1, 2, 3, 4]

print(c == d)
print(id(c))
print(id(d))
print(c is d)
