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


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self) -> None:
        self.head = None

    def push(self, data: int) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self) -> int:
        if self.is_empty():
            raise Exception("Stack is Empty")
        pop_data = self.head.data
        self.head = self.head.next
        return pop_data

    def top(self) -> int:
        if self.is_empty():
            raise Exception("Stack is Empty")
        top_data = self.head.data
        return top_data

    def is_empty(self) -> bool:
        is_empty = False
        if self.head is None:
            is_empty = True
        return is_empty


# example
print()
print("LinkedStack")
s = LinkedStack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
# print(s.pop()) # Exception
