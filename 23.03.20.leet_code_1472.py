# https://leetcode.com/problems/design-browser-history/

from __future__ import annotations


from typing import Optional


class Node:
    def __init__(self, value: str = None, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class BrowserHistory(object):
    def __init__(self, homepage: str) -> None:
        self.head = self.current = Node(homepage)

    def visit(self, url: str) -> None:
        """
        :type url: str
        :rtype: None
        """
        self.current.next = Node(value=url, prev=self.current)
        self.current = self.current.next
        return None

    def back(self, steps: int) -> str:
        """
        :type steps: int
        :rtype: str
        """
        while steps > 0 and self.current.prev != None:
            steps -= 1
            self.current = self.current.prev
        return self.current.value

    def forward(self, steps: int) -> str:
        """
        :type steps: int
        :rtype: str
        """

        while steps > 0 and self.current.next != None:
            steps -= 1
            self.current = self.current.next
        return self.current.value


# Your BrowserHistory object will be instantiated and called as such:
obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
