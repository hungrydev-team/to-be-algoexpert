from abc import abstractmethod


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedListInterface:
    @abstractmethod
    def add_first(self, node: Node) -> None:
        pass

    @abstractmethod
    def add_last(self, node: Node) -> None:
        pass

    @abstractmethod
    def remove_first(self) -> Node:
        pass

    @abstractmethod
    def remove_last(self) -> Node:
        pass

    @abstractmethod
    def search(self, index) -> Node:
        pass

    @abstractmethod
    def insert(self, index, node) -> None:
        pass

    @abstractmethod
    def remove(self, index) -> Node:
        pass


class NoSuchElementException(Exception):
    pass


class DoublyLinkedList(DoublyLinkedListInterface):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, node: Node) -> None:
        # TODO 53~57을 extract method.
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
            return
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
        return

    def add_last(self, node: Node) -> None:
        if self.size == 0:
            self.head = node
            self.tail = node
            self.size += 1
            return
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
        self.size += 1
        return

    def remove_first(self) -> Node:
        if self.head is None:
            raise NoSuchElementException()
        if self.head.next is None:
            node = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return node
        node = self.head
        node.next.prev = None
        self.head = node.next
        node.next = None
        self.size -= 1
        return node

    def remove_last(self) -> Node:
        if self.tail is None:
            raise NoSuchElementException()
        if self.tail.prev is None:
            node = self.tail
            self.head = None
            self.tail = None
            self.size -= 1
            return node
        node = self.tail
        node.prev.next = None
        self.tail = node.prev
        node.prev = None
        self.size -= 1
        return node

    def search(self, index) -> Node:
        if index > self.size:
            raise NoSuchElementException()
        if index < (self.size / 2):
            node = self.head
            count = 1
            while count != index:
                count += 1
                node = node.next
            return node
        if index > (self.size / 2):
            node = self.tail
            count = self.size
            while count != index:
                count -= 1
                node = node.prev
            return node

    def insert(self, index, node) -> None:
        if index == 0:
            self.add_first(node)
            # self.head = node
            # self.tail = node
            # self.size += 1
            return
        found_node = self.search(index - 1)
        next_found_node = found_node.next
        found_node.next = node
        node.next = next_found_node
        if next_found_node is not None:
            next_found_node.prev = node
        node.prev = found_node
        return

    def remove(self, index) -> Node:
        node = self.search(index)
        if node.prev is None:
            next_node = node.next
            node.next = None
            next_node.prev = None
            self.head = next_node
            self.size -= 1
            return node
        if node.next is None:
            prev_node = node.prev
            node.prev = None
            prev_node.next = None
            self.tail = prev_node
            self.size -= 1
            return node
        next_node = node.next
        prev_node = node.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        node.next = None
        node.prev = None
        self.size -= 1
        return Node


# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# linked_list = DoublyLinkedList()
# linked_list.insert(1, node1)
# linked_list.insert(1, node2)
