# 类只负责定义或描述一个事物的类型和原型
# 1.继承
# 2.封装
# 3.多态

# 方法设计层面、方法调用层面
# 类是现实世界中的事物在计算机中的表现现实

# 类变量和实例变量
# 实例方法、类方法、静态方法
# 方法私有名字前面添加两个下划线__
# {'__module__': '__main__', 'name': '', 'age': 0,
# 'print_file': <function Student.print_file at 0x10542e048>,
# '__dict__': <attribute '__dict__' of 'Student' objects>,
# '__weakref__': <attribute '__weakref__' of 'Student' objects>, '__doc__': None}


class Student:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_file(self):
        print(self.name)
        print(self.age)


stu = Student('aige', 20)
stu.print_file()

print(stu.__dict__)
print(Student.__dict__)
