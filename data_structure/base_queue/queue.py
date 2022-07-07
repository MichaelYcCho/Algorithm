# 선입선출구조
from typing import Deque


class Queue:
    def __init__(self):
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def enqueue(self, data):
        self.container.append(data)
    
    def dequeue(self):
        # 동적배열의 맨 처음 데이터를 삭제한 후 모든데이터를 한칸씩 옮겨야함
        # 그러므로빅오는 O(n)
        return self.container.pop(0)

    # 이건 리스트에서의 dequeue를 사용하므로 O(n)
    # 만약 collections.deque를 사용한다면 O(1)
    
    def peek(self):
        if self.empty():
            return None
        else:
            return self.container[0]
