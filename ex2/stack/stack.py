
class Stack:
    def __init__(self):
        self.__m_buffer = []

    def push(self, element):
        self.__m_buffer.append(element)

    def top(self):
        return self.__m_buffer[-1]

    def pop(self):
        self.__m_buffer.pop()

    def size(self):
        return len(self.__m_buffer)

    def is_empty(self):
        return self.size() == 0


class Stack2(Stack):
    def __init__(self):
        super().__init__()

    def get_min_value(self):
        return min(self._Stack__m_buffer)

    def print_stack(self):
        print("\nAktualnie w stosie znajudją się liczby")
        print(*self._Stack__m_buffer, sep= ", " )