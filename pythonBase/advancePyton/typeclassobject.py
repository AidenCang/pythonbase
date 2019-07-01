class Pepole(object):
    # Python对象相应获得相关的迭代，先试着找iter、next，如果找不到，会试着查找getitem
    def __iter__(self):
        pass

    def __next__(self):
        pass

    def __getitem__(self, item):
        pass
