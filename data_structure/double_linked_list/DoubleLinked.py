from double_linked_list.node import Node


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.tail = Node()
        
        # 초기화
        # head와 tail를 연결
        self.head.next = self.tail
        self.tail.prev = self.head
        
        # 데이터 개수를 저장
        self.d_size = 0
        
    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False
        
    def size(self):
        return self.d_size