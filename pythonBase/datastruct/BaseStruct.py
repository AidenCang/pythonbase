print(type(1))
print(type(1.111111111111111111111111111))
print(type(1 + 2.0))
print(type(2 / 2))
# 强制取整
print(type(2 // 2))

# 2、8、10、16进制
# 2进制
print(bin(8))
print(bin(0o7))
print(bin(0xE))
# 10进制
print(int(0b111))
print(int(0o234))
print(int(0Xc))

# 16进制
print(hex(9))
print(hex(0b1011))
print(hex(0o735))

# 8进制
print(oct(10))
print(oct(0b1011))
print(oct(0XA))

# Number：bool是Number的一个子类，只要是非零的数都表示为True
# bool
# complex 复数类型
# python中表示复数36j
# str字符串
# 如何在python表示字符串:单引号、双引号、三引号
print(r'c:\nabc')  # 添加r表示原始字符串
print(ord('A'))  # 获取字符串的ASSIC码
a = 1
print(hex(id(a)))  # 使用ID获取变量在内存中的地址

# 字符比较:ASSIC码做比较
# 字符串比较:对应位置上的字符做比较

# 列表比较使用对应位置进行比较: [2, 3, 1] > [3, 1, 3]
print([5, 3, 1] > [3, 1, 3])

# 成员运算符

# 身份运算符 is表示内存地址是否相等: a is b
# 对象的三个特征 id,value,type
# is, == ,isinstance()

# type 和 isinstance() 有什么区别
# type 不能判断子类型
# isinstance() 能够判断子类型

# Python代码不能过被压缩、混淆

# vs、linter、pylint，snippet 变量的规范
a = ['1', 'b', 'ba']

for x in a:
    if x == '1':
        break  # 使用了break之后，不会执行下面的else
    print(x)
else:
    print('end')
