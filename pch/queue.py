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


class Queue(QueueInterface):
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def enqueue(self, node: Node) -> None:
        self.size += 1
        if self.first is None:
            self.first = node
            self.last = node
            return
        self.last.next = node
        node.prev = self.last
        self.last = node
        return

    def dequeue(self) -> Node:
        if self.first is None:
            raise NoSuchElementException()
        self.size -= 1
        if self.first.next is None:
            node = self.first
            self.first = None
            self.last = None
            return node
        node = self.first
        self.first = self.first.next
        self.first.prev = None
        node.next = None
        return node

    def search(self, index) -> Node:
        if index > self.size:
            raise NoSuchElementException()
        start_index = 1
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

print(queue.search(2))

print(queue)
