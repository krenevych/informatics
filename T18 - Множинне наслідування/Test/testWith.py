

class TestContext:
    def __init__(self):
        print("__init__")

    def __enter__(self):
        print("__enter__")
        return 777

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")


with TestContext() as a:
    print(a)

