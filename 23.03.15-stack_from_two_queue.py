import queue


class Stack:
    def __init__(self) -> None:
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    def push(self, element):
        self.q1.put(element)

    def pop(self):
        # 마지막 값 앞의 값들을 q2에 넣는다.
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp

        return self.q2.get()


# example
s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())
print(s.pop())
print(s.pop())
