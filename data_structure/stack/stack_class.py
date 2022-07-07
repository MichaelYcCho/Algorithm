


class Stack:
    def __init__(self):
        self.container = list()

    def empty(self) -> bool:
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
         # 마지막 위치에 값을 삽입하므로 O(1) 
        self.container.append(data)

    def pop(self):
        if self.empty():
            return None
        else:
            # 마지막 값을 빼는것이므로 O(1) 
            return self.container.pop()

    # 스택 가장 위의 데이터를 반환 특정데이터를 찾을때까지 반복하므로 O(n)
    def peek(self):
        if self.empty():
            return None
        else:
            return self.container[-1]