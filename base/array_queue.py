"""
Queue based upon array
基于数组实现的队列
"""
from typing import Optional


class ArrayQueue:

    def __init__(self, capacity):
        self.__head = 0
        self.__tail = 0
        self.__items = []
        self.__capacity = capacity

    def enqueue(self, item) -> bool:
        """队列入队操作
        核心思想:
            head指针不动，tail指针+1
        边界情况:
            如果tail==capacity 则说明队列满了
        """
        if self.__tail == self.__capacity:
            if self.__head == 0:
                return False
            # 执行数据搬移
            for i in range(0, self.__tail - self.__head):
                self.__items[i] = self.__items[i + self.__head]
            self.__tail = self.__tail - self.__head
            self.__head = 0

        self.__items.insert(self.__tail, item)
        self.__tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        """队列出队操作
        核心思想:
            tail指针不动，head指针+1
        边界情况:
            如果tail==head，则说明队列无数据了
        """
        if self.__head == self.__tail:
            return None
        item = self.__items[self.__head]
        self.__head += 1
        return item

    def __repr__(self):
        return " ".join(item for item in self.__items[self.__head: self.__tail])
