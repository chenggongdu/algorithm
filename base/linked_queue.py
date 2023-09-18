"""
Queue base upon linked
"""

from typing import Optional


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self._next = next


class LinkedQueue:
    def __init__(self):
        self._head: Optional[None] = None
        self._tail: Optional[None] = None

    def enqueue(self, value: str):
        """入队操作
        核心操作:
            入队移动tail指针，出队移动head指针
        边界情况:
            无界队列
        """
        new_node = Node(value)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node

    def dequeue(self) -> Optional[str]:
        """出队操作
        核心操作:
            入队移动tail指针，出队移动head指针
        """
        if self._head:
            value = self._head.data
            self._head = self._head._next

            if not self._head:
                self._tail = None
            return value

    def __repr__(self) -> str:
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current._next
        return "->".join(value for value in values)


if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)
