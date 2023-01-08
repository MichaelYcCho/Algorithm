class Node:
    def __init__(self, value = 0, next = None) -> None:
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
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            # head는 항상 첫번째 노드만 가리켜야한다.
            self.head = new_node
        # 맨 뒤에 node가 new_node를 가리켜야한다. 
        else:
            current = self.head
            # current.next가 None이 될때까지 반복하며 current를 이동시킨다.
            while(current.next):
                current = current.next
            current.next = new_node


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)