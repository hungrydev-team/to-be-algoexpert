import numpy as np


class NoSuchElementException(Exception):
    pass


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, node: Node):
        if self.head is None:
            self.head = node
            return
        cursor = self.head
        while cursor.next is not None:
            cursor = cursor.next
        cursor.next = node

    def pop(self):
        if self.head is None:
            raise NoSuchElementException()
        # 헤드에만 노드가 있는 경우
        if self.head.next is None:
            last_node = self.head
            self.head = None
            return last_node
        node = self.head
        while node.next.next is not None:
            node = node.next
        last_node = node.next
        node.next = None
        return last_node

    def shift(self):
        if self.head is None:
            return NoSuchElementException()
        node = self.head
        self.head = self.head.next
        return node

    def unshift(self, node: Node):
        node.next = self.head
        self.head = node

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


class HashTable():
    def __init__(self):
        self.size = 1000
        self.list = [0 for i in range(self.size)]

    def __hash__(self, val):
        index = val % self.size
        return index

    def __setitem__(self, key, val):
        index = self.__hash__(key)
        if self.list[index] is None:
            self.list[index] = LinkedList()
            self.list[index].append(Node(key, val))
        else:
            self.list[index].append(Node(key, val))

    def __getitem__(self, key):
        index = self.__hash__(key)
        node = self.list[index].head
        while node.key != key or node is not None:
            node = node.next
        if node is None:
            return None
        else:
            return node.val


hash_table = HashTable()

hash_table[7] = 1


