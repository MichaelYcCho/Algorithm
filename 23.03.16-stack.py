class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is Empty")

        pop_object = self.stack.pop()
        return pop_object

    def top(self):
        if self.is_empty():
            raise Exception("Stack is Empty")

        top_object = self.stack[-1]
        return top_object

    def is_empty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty


# example
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
