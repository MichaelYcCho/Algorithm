from __future__ import annotations
from typing import Optional


class Node:
    def __init__(self, value: int = 0, next: Optional[Node] = None) -> None:
        self.value = value
        self.next = next


first = Node(1)
second = Node(2)
third = Node(3)

first.next = second
second.next = third
first.value = 6


class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    # Head를 통해서 맨 뒤에 node를 추가해야하므로 O(n)이다.
    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            # head는 항상 첫번째 노드만 가리켜야한다.
            self.head = new_node
            self.tail = new_node
        # 맨 뒤에 node가 new_node를 가리켜야한다.
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Head를 통해서 해당하는 인덱스 까지가야하므로 O(n)이다.
    def get(self, idx: int) -> int:
        current = self.head
        for i in range(idx):
            current = current.next
        return current.value

    def insert(self, idx: int, value: int) -> None:
        new_node = Node(value)
        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(idx - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def remove(self, idx: int) -> None:
        if idx == 0:
            # 가장 앞의 노드를 삭제하면 head는 두번째 노드를 가리켜야한다.
            # garbage collector가 알아서 처리해준다.
            self.head = self.head.next
        else:
            current = self.head
            for i in range(idx - 1):
                current = current.next
            current.next = current.next.next


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert(2, 5)
print(ll.get(2))
ll.remove(2)
print(ll.get(2))
