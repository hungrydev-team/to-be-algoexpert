from data_structure.node import Node


class LinkedList():
    def __init__(self):
        self.head = None

    def add(self, val):
        # Appends the specified element to the end of this list.
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def remove(self):
        # Retrieves and removes the head (first element) of this list.
        pass

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, "-> ", end='')
            temp = temp.next


linked_list = LinkedList()
linked_list.add(1)
linked_list.add(2)
linked_list.add(3)
linked_list.add(4)
linked_list.print_list()
