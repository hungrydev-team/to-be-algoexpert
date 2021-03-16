from abc import abstractmethod


class NoSuchElementException(Exception):
    pass


class WrongIndex(Exception):
    pass


class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None

    def __str__(self):
        result = "{ "
        result += str(self.val)
        result += " }"
        return result


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


class Stack(StackInterface):
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, node: Node) -> None:
        if self.size == 0:
            self.top = node
        else:
            node.prev = self.top
            self.top = node
        self.size += 1
        return

    def pop(self) -> Node:
        if self.size == 0:
            raise NoSuchElementException()
        elif self.size == 1:
            node = self.top
            self.top = None
        else:
            node = self.top
            self.top = self.top.prev
            node.prev = None
        self.size -= 1
        return node

    def search(self, index) -> Node:
        if index < 0 or index > self.size - 1:
            raise WrongIndex()
        node = self.top
        for i in range(index):
            node = node.prev
        return node

    def peek(self) -> Node:
        if self.size == 0:
            raise NoSuchElementException()
        return self.top

    def __str__(self):
        current_node = self.top
        result = "top\n"
        result += " |\n v\n"
        for i in range(self.size):
            result += "["
            result += str(current_node.val)
            result += "]\n |\n v\n"
            current_node = current_node.prev
        result += "None"
        return result


stack = Stack()

stack.push(Node(1))
stack.push(Node(2))
stack.push(Node(3))
stack.push(Node(4))

print(stack.pop())
print(stack.pop())

print(stack.search(1))

print(stack.peek())

print(stack)
