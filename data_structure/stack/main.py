from stack_class import Stack



if __name__ == "__main__":
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    while not s.empty():
        print(s.pop(), end='   ')
