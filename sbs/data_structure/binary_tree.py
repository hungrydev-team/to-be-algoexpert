from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, node: Node) -> None:
        cursor = self.root
        if cursor is None:
            self.root = node
            return
        while 1:
            if cursor.data < node.data:
                if cursor.right is not None:
                    cursor = cursor.right
                else:
                    cursor.right = node
                    break
            else:
                if cursor.left is not None:
                    cursor = cursor.left
                else:
                    cursor.left = node
                    break

    def delete(self):
        pass

    def search(self, node: Node) -> Optional[bool]:
        cursor = self.root
        while cursor.data is not None:
            if cursor.data == node.data:
                return True
            else:
                if cursor.data < node.data:
                    if cursor.right is not None:
                        cursor = cursor.right
                    else:
                        return False
                else:
                    if cursor.left is not None:
                        cursor = cursor.left
                    else:
                        return False


array = [51, 2, 7, 10, -31, 0, 8]
binary_tree = BinaryTree()
for i in array:
    binary_tree.insert(Node(i))
a = binary_tree.search(Node(51))
print(a)
b = binary_tree.search(Node(1))
print(b)

