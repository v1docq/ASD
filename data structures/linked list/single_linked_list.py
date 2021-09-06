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

        while current != None:
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
        while node != None:
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

        while current != None:
            if current.value == val:
                list_of_nodes.append(current)
            current = current.next
        return list_of_nodes

    def delete(self, val, all=False):
        if self.head is None:
            raise ValueError("The linked list has no element to delete")

        if self.head.value == val:
            self.head = self.head.next
            return

        count = 0
        current = self.head
        while current.next is not None:
            if current.next.value == val:
                if all:
                    count += 1
                    if current.next is None:
                        break
                    else:
                        current.next = current.next.next
                    continue
                else:
                    current.next = current.next.next
                    break
            current = current.next

        if current.next is None and count == 0:
            raise ValueError("{} was not found in list".format(val))

    def clean(self):
        return self.__init__()

    def len(self):
        return self.__len__()

    def insert(self, afterNode, newNode):

        if afterNode is None:
            self.head = afterNode

        current = self.head
        while current is not None:
            if current.value == afterNode.value:
                break
            current = current.next

        if current is None:
            raise ValueError("node not in the list")
        else:
            if type(newNode) == Node:
                new_node = newNode.value
            else:
                new_node = Node(newNode)

            new_node.next = current.next
            current.next = new_node
        return
