from abc import abstractmethod


class NoSuchElementException(Exception):
    pass


class WrongIndex(Exception):
    pass


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


class DoublyLinkedList(DoublyLinkedListInterface):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, node: Node) -> None:
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.size += 1
        return

    def add_last(self, node: Node) -> None:
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.size += 1
        return

    def remove_first(self) -> Node:
        if self.size == 0:
            raise NoSuchElementException()
        elif self.size == 1:
            node = self.head
            self.head = None
            self.tail = None
        else:
            node = self.head
            self.head = node.next
            node.next.prev = None
            node.next = None
        self.size -= 1
        return node

    def remove_last(self) -> Node:
        if self.size == 0:
            raise NoSuchElementException()
        elif self.size == 1:
            node = self.tail
            self.head = None
            self.tail = None
        else:
            node = self.tail
            self.tail = node.prev
            node.prev.next = None
            node.prev = None
        self.size -= 1
        return node

    def search(self, index) -> Node:
        if index < 0 or index > self.size - 1:
            raise WrongIndex()
        elif index < ((self.size - 1) / 2):
            foo_bar = 0
            node = self.head
            while foo_bar != index:
                foo_bar += 1
                node = node.next
            return node
        else:
            foo_bar = self.size - 1
            node = self.tail
            while foo_bar != index:
                foo_bar -= 1
                node = node.prev
            return node

    def insert(self, index, node) -> None:
        if index < 0 or index > self.size:
            raise WrongIndex()
        elif index == 0:
            self.add_first(node)
        elif index == self.size:
            self.add_last(node)
        else:
            found_node = self.search(index)
            prev_node = found_node.prev
            prev_node.next = node
            found_node.prev = node
            node.prev = prev_node
            node.next = found_node
            self.size += 1
        return

    def remove(self, index) -> Node:
        if index < 0 or index > self.size - 1:
            raise WrongIndex()
        elif index == 0:
            return self.remove_first()
        elif index == self.size - 1:
            return self.remove_last()
        else:
            node = self.search(index)
            next_node = node.next
            prev_node = node.prev
            next_node.prev = prev_node
            prev_node.next = next_node
            node.next = None
            node.prev = None
            self.size -= 1
            return node

    def __str__(self):
        node = self.head
        result = "None "
        while node is not None:
            result += "<- "
            result += str(node.value)
            result += " -> "
            node = node.next
        result += "None"
        return result


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

linked_list = DoublyLinkedList()

linked_list.add_first(node1)
linked_list.add_last(node5)
linked_list.insert(1, node2)
linked_list.insert(2, node3)
linked_list.insert(3, node4)

linked_list.remove(3)
linked_list.remove(3)
linked_list.remove_first()

print(linked_list)
