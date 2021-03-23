from abc import ABC, abstractmethod

from sbs.data_structure.node import Node


class DoublyLinkedListInterface(ABC):
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
    def search(self, node) -> int:
        pass

    @abstractmethod
    def insert(self, index, node):
        pass

    @abstractmethod
    def remove(self, index):
        pass


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


class StackInterface:
    @abstractmethod
    def push(self, node: Node) -> None:
        pass

    @abstractmethod
    def pop(self) -> Node:
        pass

    @abstractmethod
    def search(self, index) -> Node:
        pass

    @abstractmethod
    def peek(self) -> Node:
        pass

    @abstractmethod
    def __str__(self):
        pass
