# 列表生成式(列表推导式)
# 1.提取1-20之间的奇数
# 列表生成式的效率高于类别操作
# 生成式表达式
# 字典推导式
# 集合推导式

odd_list = []

for i in range(21):
    if i % 2 == 0:
        odd_list.append(i)

print(odd_list)

new_list = [i for i in range(21) if i % 2 == 0]

print(new_list)
