from stack import Stack
from ex2.stack.stack import Stack2
import random

def main():

    stack = Stack2()

    for i in range(5):
        stack.push(random.randrange(1, 10))
        stack.print_stack()
        print(f"Najmniejszy element ze stosu: {stack.get_min_value()} ")


if '__main__' == __name__:
    main()
