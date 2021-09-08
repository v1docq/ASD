class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        current = self.head
        count = 0

        if self.head is None:
            return count

        while current is not None:
            count += 1
            current = current.next
        return count

    def add_in_tail(self, item):

        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        if self.head is None:
            raise ValueError("List has no elements")

        current = self.head
        list_of_nodes = []

        while current is not None:
            if current.value == val:
                list_of_nodes.append(current)
            current = current.next
        return list_of_nodes

    def delete(self, val, all=False):

        if self.head is None:
            raise ValueError("The list has no element to delete")

        if self.head.value == val:
            self.head = self.head.next
            return

        if all:
            self._delete_node_duplicates(val)
            self._delete_one_node(val)
        else:
            self._delete_one_node(val)

    def _delete_one_node(self, val):
        current = self.head
        while current.next is not None:
            if current.next.value == val:
                break
            current = current.next

        if current.next is None:
            raise ValueError("{} was not found in list".format(val))
        else:
            current.next = current.next.next

    def _delete_node_duplicates(self, val):
        current = self.head
        node_list = []
        previous_node = None
        while current is not None:
            if current.value in node_list and current.value == val:
                previous_node.next = current.next
                current = current.next
            else:
                node_list.append(current.value)
                previous_node = current
                current = current.next

    def clean(self):
        return self.__init__()

    def len(self):
        return self.__len__()

    def insert(self, afterNode, newNode):

        if self.head is None:
            print('Linked List is empty, cannot find {}'.format(newNode))
            return False

        if afterNode is None:
            afterNode = self.head

        current = self.head
        while current:
            if current.value == afterNode.value:
                break
            current = current.next

        if current is None:
            raise ValueError("Node not in the list")
        else:
            if type(newNode) == Node:
                new_node = newNode.value
            else:
                new_node = Node(newNode)

            new_node.next = current.next
            current.next = new_node
        return
