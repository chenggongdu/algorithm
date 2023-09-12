"""
 使用单向链表实现回文串判断
"""

import sys
from base.singly_linked_list import SinglyLinkedList

# 引用当前文件夹下的single_linked_list
sys.path.append('base/singly_linked_list')


def reverse(head):
    """链表返转
    核心思想:
        a -> b -> c -> d -> None
        a -> None
        b -> a -> None
        c -> b -> a -> None
        d -> c -> b -> a -> None
    :param head: 要反转的Node节点
    :return:
    """
    reverse_head = None
    while head is not None:
        next_node = head.next_node
        head.next_node = reverse_head
        reverse_head = head
        head = next_node

    return reverse_head


def is_palindrome(head_node):
    """判断head_node是否是回文
    核心思想:
        通过快慢指针找到链表的中间分隔点
        反转slow_node，同时分隔head_node, 分别比对head_node和slow_node,值都相同说明是回文串
    :param head_node: 一个字符一个字符的单链表
    :return: True-是回文串  False-不是回文串
    """
    head_node.print_all()
    slow = head_node.head_node
    fast = head_node.head_node
    position = 0
    while fast is not None and fast.next_node is not None:
        slow = slow.next_node
        fast = fast.next_node.next_node
        position += 1
    reverse_node = reverse(slow)
    head_node = head_node.head_node
    is_palin = True
    while head_node and reverse_node:
        if head_node.data == reverse_node.data:
            head_node = head_node.next_node
            reverse_node = reverse_node.next_node
        else:
            is_palin = False
            break

    return is_palin


if __name__ == '__main__':
    # the result should be False, True, True, True, True
    test_str_arr = ['abcba']
    for arr in test_str_arr:
        sll = SinglyLinkedList()
        for i in arr:
            sll.insert_to_head(i)

        print(is_palindrome(sll))
