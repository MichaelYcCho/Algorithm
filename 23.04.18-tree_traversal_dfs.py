from collections import deque


class Node:
    def __init__(self, value: int = 0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def dfs(self, cur_node: Node):
        """
        # 트리 순회
        # 스택을 이용한 방식과 재귀를 이용한 방식 2가지로 나눠진다
        여기선 재귀를 사용한다.
        # 모든 노드를 한번씩 방문해야하므로 완전탐색이라고도 불린다(깊이우선 탐색)
        1진 트리 A(Root) B(Left) C(Right)가 있다고 가정하면
        A -> B -> A -> C -> A 순으로 탐색한다

        A(Root) B C (1진의 Left, Right) D E(2진의 Left, Right)
        라면
        A -> B -> D -> B -> A -> C -> E -> C -> A 순으로 탐색한다
        """

        if cur_node is None:
            return []

        self.dfs(cur_node.left)
        self.dfs(cur_node.right)


bt = BinaryTree()
bt.root = Node(value=1)
bt.root.left = Node(value=2)
bt.root.right = Node(value=3)
bt.root.left.left = Node(value=4)
bt.root.left.right = Node(value=5)
bt.root.right.right = Node(value=6)

print(bt.dfs(bt.root))
