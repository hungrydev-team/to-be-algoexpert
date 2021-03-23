from typing import Optional

from sbs.data_structure.exception import OutOfIndex


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MyQueue:
    # FIFO
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def enqueue(self, node) -> None:
        if self.is_empty():
            self.head = node
            self.tail = node
        else:
            self.tail.prev = node
            node.next = self.tail
            self.tail = node
        self.size += 1
        return

    def dequeue(self) -> Optional[Node]:
        if self.is_empty():
            return
        elif self.size == 1:
            node = self.tail
            self.tail = None
            self.head = None
        else:
            node = self.head
            self.head = node.prev
            node.prev.next = None
            self.size -= 1
        self.size -= 1
        return node

    def search(self, index):
        if index < 0 or self.size < index:
            raise OutOfIndex("out of index")
        else:
            cursor = self.tail
            for i in range(index):
                cursor = cursor.next
            return cursor

    def print_queue(self):
        temp = self.tail
        print("tail -> ", end="")
        while temp:
            print(temp.data, "-> ", end="")
            temp = temp.next
        print("head")


queue = MyQueue()
queue.enqueue(Node(1))
queue.enqueue(Node(2))
queue.enqueue(Node(3))
queue.enqueue(Node(4))
queue.enqueue(Node(4))
queue.print_queue()
