# 容器序列:list/tuple/deque
# 扁平序列:str/bytes/bytearray/array 可用for循环遍历
# 可变序列:list/deque/bytearray/array
# 不可变：str、tuple、tytes
import numbers  # 列出Python中的数据类型
import bisect  # 用来处理已排序的的序列

a = [1, 2]
print(id(a))
a += [3, 4]
print(id(a))

a = 'abc'
print(id(a))
a += 'de'
print(id(a))
abc = list