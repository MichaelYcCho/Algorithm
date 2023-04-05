class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def reverse_linked_list(head):
    """
    연결 리스트를 반전시키는 함수

    :param head: 연결 리스트의 머리 노드
    :return: 반전된 연결 리스트의 머리 노드
    """
    # 현재 노드와 이전 노드를 초기화합니다.
    current = head
    prev = None

    # 연결 리스트를 순회하면서 노드들의 방향을 역순으로 변경
    while current:
        # 다음 노드를 임시로 저장
        next_node = current.next

        # 현재 노드의 next를 이전 노드로 변경
        current.next = prev

        # 현재 노드와 이전 노드를 한 칸씩 앞으로 이동
        prev = current
        current = next_node

    # 반전된 연결 리스트의 머리 노드를 반환
    return prev


# print value of reversed linked list
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
reversed_head = reverse_linked_list(head)

current = reversed_head
while current:
    print(current.value, end=" -> ")
    current = current.next
print("None")
