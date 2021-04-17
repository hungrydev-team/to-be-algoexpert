from abc import abstractmethod

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = None
        self.right = None


class NoSuchValue(Exception):
    pass


class BinaryTreeInterface:
    @abstractmethod
    def insert(self, node: Node) -> None:
        pass

    @abstractmethod
    def search(self, val: int) -> Node:
        pass

class BinaryTree(BinaryTreeInterface):
    def __init__(self):
        self.root = None

    def insert(self, node: Node) -> None:
        if self.root is None:
            self.root = node
            return
        cursor = self.root
        while 1:
            if node.val < cursor.val:
                if cursor.left is not None:
                    cursor = cursor.left
                else:
                    cursor.left = node
                    break
            else:
                if cursor.right is not None:
                    cursor = cursor.right
                else:
                    cursor.right = node
                    break

    def search(self, val) -> Node:
        cursor = self.root
        while cursor is not None:
            if cursor.val == val:
                return cursor
            else:
                if cursor.val < val:
                    if cursor.right is not None:
                        cursor = cursor.right
                    else:
                        raise NoSuchValue()
                else:
                    if cursor.left is not None:
                        cursor = cursor.left
                    else:
                        raise NoSuchValue()
