"""a simple browser realize
核心思想:
    1. 使用两个栈x,y.
    2. 把首次浏览的页面依次放入X栈中。
    3. 当点击后退按钮时，再依次从X栈出栈，放入Y栈中。
    4. 当点击前进按钮时。再依次从Y栈中出栈，放入X栈中。
    当栈Y中没有数据，说明没有前进的页面。
    当栈X中没有数据，说明没有后退的页面。
"""

import sys
from base.linked_stack import LinkedStack

sys.path.append("base/linked_stack.py")


class NewLinkedStack(LinkedStack):
    def is_empty(self):
        return not self._top


class Browser:

    def __init__(self):
        self.__forward_stack = NewLinkedStack()
        self.__back_stack = NewLinkedStack()

    def can_forward(self):
        if self.__back_stack.is_empty():
            return False
        return True

    def can_back(self):
        if self.__forward_stack.is_empty():
            return False
        return True

    def open(self, url: str):
        print("Open new url %s" % url, end="\n")
        self.__forward_stack.push(url)

    def back(self):
        if not self.can_back():
            return
        top = self.__forward_stack.pop()
        self.__back_stack.push(top)
        print("back to %s" % top, end="\n")

    def forward(self):
        if not self.can_forward():
            return
        top = self.__back_stack.pop()
        self.__forward_stack.push(top)
        print("forward to %s" % top, end="\n")


if __name__ == "__main__":
    browser = Browser()
    browser.open('a')
    browser.open('b')
    browser.open('c')
    if browser.can_back():
        browser.back()

    if browser.can_forward():
        browser.forward()

    browser.back()
    browser.back()
    browser.back()
    browser.back()
    browser.back()
