from abc import abstractmethod

from data_structure.node import Node


class StackInterface:
    @abstractmethod
    def push(self, node: Node) -> None:
        pass

    @abstractmethod
    def pop(self) -> Node:
        pass

    @abstractmethod
    def search(self, index) -> Node:
        pass

    @abstractmethod
    def peek(self) -> Node:
        pass

    @abstractmethod
    def __str__(self):
        pass


class MyStack(StackInterface):
    # LIFO
    def __init__(self):
        self.top = None

    def search(self, index) -> Node:
        pass

    def pop(self):
        # 스택에서 가장 위에 있는 항목을 제거한다.
        if self.top is None:
            return
        self.top = self.top.next

    def push(self, item):
        # item 하나를 스택의 가장 윗 부분에 추가한다.
        new_node = Node(item)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def peek(self):
        # 스택의 가장 위에 잇는 항목을 반환한다.
        if self.top is not None:
            return self.top.data
        return None

    def is_empty(self):
        # 스택이 비어 있을 때에 true를 반환한다.
        if self.top is None:
            return True
        return False

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.data, "-> ", end='')
            temp = temp.next
        print()


stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.print_stack()
