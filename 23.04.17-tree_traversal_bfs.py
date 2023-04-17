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
        템플릿화해서 외우자
        """
        visited = []
        if root is None:
            return 0
        q = deque()
        q.append(root)
        while q:
            cur_node = q.popleft()
            visited.append(cur_node.value)

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
