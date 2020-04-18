class MyIterator:

    def __init__(self, max_val):
        self.__max_val = max_val
        self.__a = 0
        self.__b = 1
        self.__counter = 0

    def __iter__(self):
        return self

    def __next__(self):

        self.__b = self.__a + self.__b
        self.__a = self.__b - self.__a

        if self.__counter == self.__max_val:
            raise StopIteration
        else:
            self.__counter += 1
            return self.__a


def main():

    obj = MyIterator(10)
    it = iter(obj)
    for el in it:
        print(el)


if __name__ == "__main__":
    main()
