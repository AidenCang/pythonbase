class User:
    def __new__(cls, *args, **kwargs):
        # 2.3之后才会用,控制对象的生成过程，在对象生成之前，如果new不返回对象，不会调用init对象
        print("__new__")
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        print("__init__")


if __name__ == '__main__':
    user = User("Aige")
