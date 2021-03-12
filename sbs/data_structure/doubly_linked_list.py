from typing import Optional, Tuple

from sbs.data_structure.exception import OutOfIndex, NoSuchElementException
from sbs.data_structure.structure_interface import DoublyLinkedListInterface


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(DoublyLinkedListInterface):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, node: Node) -> None:
        self.size += 1
        if self.head is None:
            self.head = node
            self.tail = node
            return
        self.head.prev = node
        node.next = self.head
        self.head = node
        return

    def add_last(self, node: Node) -> None:
        if self.size == 0:
            self.add_first(node)
            return
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

    # remove(index -> int) 메서드에서 index에 마지막 값을 전달하면 되는거 아닌가??
    def remove_last(self) -> None:
        self.remove(self.size - 1)

    def search(self, node) -> Optional[Tuple[int, Node]]:
        index = 0
        if self.head is None:
            print("빈 리스트입니다.")
            return
        cursor = self.head
        while cursor is not None:
            if cursor.data == node.data:
                break
            cursor = cursor.next
            index += 1
        if index < self.size:
            print(f"{node.data}는 index가 {index}에 존재합니다.")
            return index, cursor
        else:
            print(f"{node.data}는 리스트에 존재하지 않습니다.")
            return

    def search_index(self, index):
        if self.size < index or index < 0:
            raise NoSuchElementException()
        if index < (self.size / 2):
            cursor = self.head
            for i in range(index):
                cursor = cursor.next
            return cursor
        else:
            cursor = self.tail
            for i in range(self.size - 1, index, -1):
                cursor = cursor.prev
            return cursor

    def insert(self, index, node):
        if index < 0 or index > self.size:
            raise OutOfIndex()
        elif index == 0:
            self.add_first(node)
        elif index == self.size:
            self.add_last(node)
        else:
            found_node = self.search_index(index)
            prev_node = found_node.prev
            prev_node.next = node
            found_node.prev = node
            node.prev = prev_node
            node.next = found_node
            self.size += 1

    def remove(self, index) -> Node:
        if index < 0 or self.size < index:
            raise OutOfIndex("out of index")
        elif index == 0:
            return self.remove_first()
        else:
            temp = self.search_index(index - 1)
            delete_node = temp.next
            temp.next = temp.next.next
            if temp.next is not None:
                temp.next.prev = temp
            if delete_node == self.tail:
                self.tail = temp
            self.size -= 1
            return delete_node.data

    def display(self):
        current = self.head
        if self.head is None:
            print("List is empty")
            return
        print("Nodes of doubly linked list: ")
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()


doubly_linked_list = DoublyLinkedList()
doubly_linked_list.display()
doubly_linked_list.add_first(Node(10))
doubly_linked_list.add_first(Node(1))
doubly_linked_list.add_first(Node(2))
doubly_linked_list.add_first(Node(4))
doubly_linked_list.display()
# a = doubly_linked_list.search_index(3)
# doubly_linked_list.display()
doubly_linked_list.insert(1, Node(100))
doubly_linked_list.display()
