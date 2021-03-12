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
        self.last = None
        self.size = 0

    def push(self, node: Node) -> None:
        if self.last is None:
            self.last = node
        else:
            node.prev = self.last
            self.last = node
        self.size += 1
        return

    def pop(self) -> Node:
        if self.last is None:
            raise NoSuchElementException()
        if self.last.prev is None:
            node = self.last
            self.last = None
        else:
            node = self.last
            self.last = self.last.prev
            node.prev = None
        self.size -= 1
        return node

    def search(self, index) -> Node:
        if index < 0 or index > self.size - 1:
            raise WrongIndex()
        start_index = 0
        node = self.last
        while start_index != index:
            start_index += 1
            node = node.prev
        return node

    def peek(self) -> Node:
        if self.last is None:
            raise NoSuchElementException()
        return self.last

    def __str__(self):
        current_node = self.last
        result = "last\n"
        result += " |\n v\n"
        while current_node is not None:
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
