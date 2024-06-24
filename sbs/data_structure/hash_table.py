from logging import info
from typing import Optional

from sbs.data_structure.node import Node


class LinkedList:
    def __init__(self):
        self.head: Optional[Node] = None

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def search(self, key):
        cursor = self.head
        while cursor is not None:
            if cursor.data.data[0] == key:
                return cursor.data
            cursor = cursor.next
        return


class NoSuchKeyException(Exception):
    pass


class HashTable:
    def __init__(self, capacity: int = 1000) -> None:
        self.array = [LinkedList()] * capacity
        self.capacity = capacity

    def insert(self, key: int, value: int) -> None:
        index = self._hash(key)
        linked_list = self.array[index]
        linked_list.add(Node((key, value)))

    def remove(self, key: int) -> None:
        index = self._hash(key)
        linked_list = self.array[index]
        result = linked_list.search(key)
        if result is None:
            raise NoSuchKeyException(f"No such key: {key}")
        self.array[index] = LinkedList()
        info(f"remove를 한 key 값: {key} / value 값: {result.data[1]}")
        return result.data[1]

    def lookup(self, key: int) -> int:
        index = self._hash(key)
        linked_list = self.array[index]
        result = linked_list.search(key)
        if result is None:
            raise NoSuchKeyException(f"No such key: {key}")
        return result.data[1]

    @staticmethod
    def _hash(key):
        return key % 100
