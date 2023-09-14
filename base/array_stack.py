"""使用数组结构实现栈结构
"""


class ArrayStack:
    """数组链表
    """

    def __init__(self, count: int):
        """构造器初始化
        入参:
            count: 数组栈的最大个数
        """
        self.__count = count
        self.__array = []
        self.__current_count = 0

    def push(self, data):
        """向数组栈添加一个元素
        """
        if len(self.__array) >= self.__count:
            return
        self.__current_count += 1
        self.__array.append(data)

    def pop(self):
        """从数组栈弹出一个元素
        """
        if len(self.__array) == 0:
            return
        self.__current_count -= 1
        return self.__array.pop(self.__current_count)

    def __repr__(self):
        return f"{' '.join(f'{value}]' for value in self.__array)} current_count = {self.__current_count}"


if __name__ == "__main__":
    array = ArrayStack(3)
    array.push(1)
    array.push(2)
    array.push(3)
    # 1] 2] 3] current_count = 3
    print(array)
    array.pop()
    # 1] 2] current_count = 2
    print(array)
    array.pop()
    # 1] current_count = 1
    print(array)
