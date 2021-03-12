from abc import abstractmethod

from data_structure.node import Node


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


class MyQueue:
    # FIFO
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def enqueue(self, item):
        # item을 리스트의 끝부분에 추가한다.
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

    def dequeue(self):
        # 리스트의 첫 번재 항목을 제거한다.
        if self.is_empty():
            return
        temp = self.head
        self.head = temp.next
        if self.head is None:
            self.tail = None

    def print_queue(self):
        temp = self.head
        while temp:
            print(temp.data, "-> ", end='')
            temp = temp.next


queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.dequeue()
queue.print_queue()
