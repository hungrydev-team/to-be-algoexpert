from abc import abstractmethod


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self):
        result = "{ "
        result += str(self.val)
        result += " }"
        return result


class QueueInterface:
    @abstractmethod
    def enqueue(self, node: Node) -> None:
        pass

    @abstractmethod
    def dequeue(self) -> Node:
        pass

    @abstractmethod
    def search(self, index) -> Node:
        pass

    @abstractmethod
    def __str__(self):
        pass


class NoSuchElementException(Exception):
    pass


class WrongIndex(Exception):
    pass


class Queue(QueueInterface):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, node: Node) -> None:
        if self.first is None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
        self.size += 1
        return

    def dequeue(self) -> Node:
        if self.first is None:
            raise NoSuchElementException()
        if self.first.next is None:
            node = self.first
            self.first = None
            self.last = None
        else:
            node = self.first
            self.first = self.first.next
            self.first.prev = None
            node.next = None
        self.size -= 1
        return node

    def search(self, index) -> Node:
        if index < 0 or index > self.size - 1:
            raise WrongIndex()
        start_index = 0
        node = self.first
        while start_index != index:
            start_index += 1
            node = node.next
        return node

    def peek(self) -> Node:
        if self.first is None:
            raise NoSuchElementException()
        return self.first

    def __str__(self):
        node = self.first
        result = "None "
        while node is not None:
            result += "<- "
            result += str(node.val)
            result += " -> "
            node = node.next
        result += "None"
        return result


queue = Queue()

queue.enqueue(Node(1))
queue.enqueue(Node(2))
queue.enqueue(Node(3))
queue.enqueue(Node(4))

print(queue.dequeue())
print(queue.dequeue())

print(queue.peek())

print(queue.search(0))

print(queue)
