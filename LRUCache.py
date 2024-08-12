class DLLNode:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None


class LRUCache:
    # 가장 오래된 노드 순으로 배치한다.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # 해시맵: 키 -> 노드
        self.head = DLLNode(0, 0)  # 더미 헤드
        self.tail = DLLNode(0, 0)  # 더미 테일
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: DLLNode):
        # 노드를 제거
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add_node(self, node: DLLNode):
        # 노드를 리스트의 끝에 추가
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def _move_to_end(self, node: DLLNode):
        # 노드를 리스트의 끝으로 이동 (가장 최근 사용으로 간주)
        self._remove_node(node)
        self._add_node(node)

    def _pop_from_front(self):
        # 가장 오래된 노드 제거 (헤드 다음 노드)
        node = self.head.next
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._move_to_end(node)  # 순서변경 (사용된 노드를 리스트 끝으로)
            return node.data
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # 기존 노드를 업데이트하고 끝으로 이동
            node = self.cache[key]
            node.data = value
            self._move_to_end(node)
        else:
            # 새 노드를 추가
            if len(self.cache) >= self.capacity:
                # 용량 초과 시 가장 오래된 노드 제거(맨앞)
                oldest_node = self._pop_from_front()
                del self.cache[oldest_node.key]
            new_node = DLLNode(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
