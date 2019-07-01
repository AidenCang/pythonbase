# 面向对象
# 1.封装
# 2.多态
# 3.继承


class Hamman:
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def print_han(self):
        print(Hamman.__name__)


class Student(Hamman):
    def __init__(self, score):
        self.score = score
        super(Student, self).__init__(name='aige', age='20', score=99)

    def print_sut(self):
        print(self.name)
        print(self.age)
        print(self.score)
        self.print_han()


stu = Student(20)
stu.print_sut()
