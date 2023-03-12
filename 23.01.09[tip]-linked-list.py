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

    # Head를 통해서 맨 뒤에 node를 추가해야하므로 O(n)이다.
    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.head is None:
            # head는 항상 첫번째 노드만 가리켜야한다.
            self.head = new_node
        # 맨 뒤에 node가 new_node를 가리켜야한다.
        else:
            current = self.head
            # current.next가 None이 될때까지 반복하며 current를 이동시킨다.
            while current.next:
                current = current.next
            current.next = new_node

    # Head를 통해서 해당하는 인덱스 까지가야하므로 O(n)이다.
    def get(self, idx: int) -> int:
        current = self.head
        for i in range(idx):
            current = current.next
        return current.value


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
