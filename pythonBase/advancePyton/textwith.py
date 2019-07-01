class Sample:

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__enter__")

    def do_something(self):
        print("do_something")


if __name__ == '__main__':
    with Sample() as sample:
        sample.do_something()


