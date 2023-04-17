from collections import deque


class Node:
    def __init__(self, value: int = 0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    @staticmethod
    def bfs(root):
        """
        # 트리 순회
        # 모든 노드를 한번씩 방문해야하므로 완전탐색이라고도 불린다
        같은 레벨 노드들을 먼저 탐색하고 다음 레벨 노드들을 탐색한다(횡으로 탐색)
        템플릿화해서 외우자
        """
        visited = []
        if root is None:
            return []
        q = deque()  # 큐 q:[], bfs를 위해선 큐가 필요하다 FIFO 구조라 먼저 Queue에 들어간 node가 먼저 나온다
        q.append(root)
        while q:
            # 처음엔 root_node 접근
            cur_node = q.popleft()
            visited.append(cur_node.value)

            # 왼쪽, 오른쪽 자식 노드가 있으면 큐에 추가
            # 결과적으로 다시 while문을 돌면서 왼쪽, 오른쪽 자식 노드를 계속 접근
            if cur_node.left:
                q.append(cur_node.left)
            if cur_node.right:
                q.append(cur_node.right)
        return visited


bt = BinaryTree()
bt.root = Node(value=1)
bt.root.left = Node(value=2)
bt.root.right = Node(value=3)
bt.root.left.left = Node(value=4)
bt.root.left.right = Node(value=5)
bt.root.right.right = Node(value=6)

print(bt.bfs(bt.root))
