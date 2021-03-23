from sbs.data_structure.exception import NoSuchElementException
from sbs.data_structure.node import Node
from sbs.data_structure.structure_interface import StackInterface


class MyStack(StackInterface):
    # LIFO
    def __init__(self):
        self.top = None
        self.size = 0

    def search(self, index) -> Node:
        if index < 0 or self.size < index:
            raise NoSuchElementException("index 밖입니다.")
        else:
            cursor = self.top
            for i in range(index):
                cursor = cursor.next
            return cursor

    def pop(self):
        # 스택에서 가장 위에 있는 항목을 제거한다.
        if self.top is None:
            return
        self.top = self.top.next
        self.size -= 1

    def push(self, node):
        # item 하나를 스택의 가장 윗 부분에 추가한다.
        if self.is_empty():
            self.top = node
            self.size += 1
        else:
            node.next = self.top
            self.top = node
            self.size += 1

    def peek(self):
        # 스택의 가장 위에 잇는 항목을 반환한다.
        if self.is_empty():
            return NoSuchElementException()
        return self.top.data

    def is_empty(self):
        # 스택이 비어 있을 때에 true를 반환한다.
        return self.size == 0

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.data, "-> ", end='')
            temp = temp.next
        print()


stack = MyStack()
stack.push(Node(1))
stack.push(Node(2))
stack.push(Node(3))
stack.push(Node(4))
stack.print_stack()
a = stack.search(0)
stack.pop()
stack.print_stack()
