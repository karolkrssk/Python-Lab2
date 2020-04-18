from functools import wraps


class MyDeco:
    def __init__(self, func):
        self.__func = func
        wraps(self.__func)

    def __call__(self, *args, **kwargs):
        print(
            f"Aktualna ilość wywołań funcji to: {my_function.counter}")
        return self.__func(*args, **kwargs)


@MyDeco
def my_function():
    my_function.counter += 1
    print("do something...")


def main():
    my_function.counter = 1
    my_function()
    my_function()
    my_function()


if __name__ == "__main__":
    main()
