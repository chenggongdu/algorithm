from typing import Optional


class Node:
    """链表数据存储"""

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


class LinkedStack:
    """a stack based upon singly-linked list
    """

    def __init__(self):
        self._top = None

    def push(self, value):
        """ 向链表栈中添加一个元素
        :param value: Node存储的值
        :return: void
        """
        new_top: Node = Node(value)
        new_top.next = self._top
        self._top = new_top

    def pop(self):
        """从链表栈中取出一个元素
        :return: 返回取出的元素 || None
        """
        if self._top:
            value = self._top.data
            self._top = self._top.next
            return value

    def __repr__(self):
        current = self._top
        objs = []
        while current:
            objs.append(current.data)
            current = current.next
        return " ".join(f"{obj}]" for obj in objs)


if __name__ == "__main__":
    """
    8] 7] 6] 5] 4] 3] 2] 1] 0]
    5] 4] 3] 2] 1] 0]
    """
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)

    for _ in range(3):
        stack.pop()

    print(stack)
