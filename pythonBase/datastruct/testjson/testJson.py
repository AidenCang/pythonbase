import json

# json        python
# object      dict
# array       list
# string      str
# number      int
# number      float
# true        True
# false       False
# null        None

# Json/JSON对象、JSON字符串

json_str = '{"name":"aige","age" :20}'
res = json.loads(json_str)
print(type(res))
print(res)
print(res['name'])
print(res['age'])
