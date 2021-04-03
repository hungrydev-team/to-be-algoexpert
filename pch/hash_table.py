from abc import abstractmethod


class WrongIndex(Exception):
    pass


class NoSuchKeyException(Exception):
    pass


class NoSuchElementException(Exception):
    pass


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class HashTableInterface:
    @abstractmethod
    def insert(self, key: int, value: int) -> None:
        pass

    @abstractmethod
    def remove(self, key: int) -> None:
        pass

    @abstractmethod
    def lookup(self, key: int) -> int:
        pass


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

    @abstractmethod
    def search_by_key(self, key) -> Node or None:
        pass

    @abstractmethod
    def remove_by_key(self, key) -> Node or None:
        pass


class LinkedList(LinkedListInterface):
    def __init__(self):
        self.head = None
        self.size = 0

    def add_last(self, node: Node) -> None:
        if self.head is None:
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
        if self.head is None:
            raise NoSuchElementException()
        # 헤드에만 노드가 있는 경우
        elif self.head.next is None:
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
        if self.head is None:
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

    def search_by_key(self, key) -> Node or None:
        node = self.head
        for i in range(self.size - 1):
            if node.key == key:
                return node
            node = node.next
        return

    def remove_by_key(self, key) -> Node or None:
        node = self.search_by_key(key)
        if node is None:
            return
        elif node is self.head:
            return self.remove_first()
        elif node.next is None:
            return self.remove_last()
        else:
            cursor = self.head
            for i in range(self.size - 2):
                if cursor.next is node:
                    break
                cursor = cursor.next
            cursor.next = node.next
            node.next = None
            return node

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


class HashTable(HashTableInterface):
    def __init__(self, capacity: int = 1000) -> None:
        self.capacity = capacity
        self.array = [LinkedList()] * self.capacity

    def _hash(self, val: int) -> int:
        index = val % self.capacity
        return index

    def insert(self, key: int, value: int) -> None:
        linked_list = self.get_linked_list_by_key(key)
        linked_list.add_last(Node(key, value))
        return

    def remove(self, key: int) -> None:
        linked_list = self.get_linked_list_by_key(key)
        return linked_list.remove_by_key(key)

    def get_linked_list_by_key(self, key):
        index = self._hash(key)
        linked_list = self.array[index]
        return linked_list

    def lookup(self, key: int) -> int or None:
        linked_list = self.get_linked_list_by_key(key)
        return linked_list.search_by_key(key).val


hash_table = HashTable()

hash_table.insert(11, 26)
hash_table.insert(4, 16)
# print(hash_table.lookup(11))
# print(hash_table.lookup(4))
# print(hash_table.remove(4))
# print(hash_table.lookup(4))
