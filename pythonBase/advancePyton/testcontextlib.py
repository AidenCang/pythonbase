import contextlib


@contextlib.contextmanager
def open_file(file):
    print('open')
    yield {}  # 生成器的使用
    print('close')


with open_file("textcontextlib") as file:
    print("操作文件")
