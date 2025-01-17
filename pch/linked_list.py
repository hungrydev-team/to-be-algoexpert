from abc import abstractmethod


class WrongIndex(Exception):
    pass


class NoSuchElementException(Exception):
    pass


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return f"{ {self.val} }"


class LinkedListInterface:
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


class LinkedList(LinkedListInterface):
    def __init__(self):
        self.head = None
        self.size = 0

    def add_last(self, node: Node) -> None:
        if self.size == 0:
            self.head = node
        else:
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = node
        self.size += 1
        return

    def remove_last(self) -> Node:
        # 헤드에 노드가 없는 경우
        if self.size == 0:
            raise NoSuchElementException()
        # 헤드에만 노드가 있는 경우
        elif self.size == 1:
            last_node = self.head
            self.head = None
        else:
            node = self.head
            while node.next.next is not None:
                node = node.next
            last_node = node.next
            node.next = None
        self.size -= 1
        return last_node

    def remove_first(self) -> Node:
        if self.size == 0:
            return NoSuchElementException()
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node

    def add_first(self, node: Node) -> None:
        node.next = self.head
        self.head = node
        self.size += 1
        return

    def search(self, index) -> Node:
        if index < 0 or index > self.size - 1:
            return WrongIndex()
        node = self.head
        for i in range(index):
            node = node.next
        return node

    def remove(self, index) -> Node:
        if index < 0 or index > self.size - 1:
            return WrongIndex()
        elif index == 0:
            return self.remove_first()
        elif index == self.size - 1:
            return self.remove_last()
        else:
            prev_node = self.search(index - 1)
            next_node = prev_node.next.next
            node = prev_node.next
            prev_node.next = next_node
            node.next = None
            self.size -= 1
            return node

    def insert(self, index, node) -> None:
        if index < 0 or index > self.size:
            return WrongIndex()
        elif index == 0:
            return self.add_first(node)
        elif index == self.size:
            return self.add_last(node)
        else:
            prev_node = self.search(index - 1)
            next_node = prev_node.next
            prev_node.next = node
            node.next = next_node
            self.size += 1
            return

    def __str__(self):
        current_node = self.head
        if current_node is None:
            return "{}"
        output = "{"
        output += str(current_node.val)
        while current_node.next is not None:
            current_node = current_node.next
            output += " -> "
            output += str(current_node.val)
        output += "}"
        return output


linked_list = LinkedList()

linked_list.add_first(Node(1))
linked_list.add_first(Node(2))
linked_list.add_first(Node(3))

linked_list.add_last(Node(4))
linked_list.insert(3, Node(5))
linked_list.insert(0, Node(6))
linked_list.insert(6, Node(7))

print(linked_list.search(4))

linked_list.remove_first()
linked_list.remove_last()
linked_list.remove(2)
linked_list.remove(0)
linked_list.remove(2)

print(linked_list)
