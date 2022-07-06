


class Stack:
    def __init__(self):
        self.container = list()

    def empty(self) -> bool:
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if self.empty():
            return None
        else:
            return self.container.pop()

    # 스택 가장 위의 데이터를 반환
    def peek(self):
        if self.empty():
            return None
        else:
            return self.container[-1]