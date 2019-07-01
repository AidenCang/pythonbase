class Book:
    def __init__(self):
        self.data = ['往事', '智能', '回味']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration()
        res = self.data[self.index]
        self.index += 1
        return res


print(id(None))
print(type(None))
