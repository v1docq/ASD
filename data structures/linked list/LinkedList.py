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
        # Проверка на пустой лист
        if self.head is None:
            raise ValueError("The linked list has no element to delete")

        # Начинаем с главы списка и итеративно движемся пока не найдем искомое значение (afterNode)
        if self.head.value == val:
            self.head = self.head.next
            return

        count = 0
        current = self.head
        # Два условия цикла. Первое что следующием элменет не null (то есть мы не в конце списка).
        while current.next is not None:
            # Второе то что если значение следующего узла равно искомому у нас есть два варианта действовать
            if current.next.value == val:
                # Удаляем все элементы
                if all:
                    count += 1
                    # Если мы на предпоследнем элементе то выходим из цикла
                    if current.next is None:
                        break
                    # Если нет, то переводим указатель на +1 элемент
                    else:
                        current.next = current.next.next
                    continue
                # Удаляем 1 элемент и выходим из цикла
                else:
                    current.next = current.next.next
                    break
            # Итерация по циклу
            current = current.next

        # Проверка на отсутствие элемента
        if current.next is None and count == 0:
            raise ValueError("{} was not found in list".format(val))

    def clean(self):
        return self.__init__()

    def len(self):
        return self.__len__()

    def insert(self, afterNode, newNode):

        if afterNode is None:
            self.head = afterNode

        # Начинаем с главы списка и итеративно движемся пока не найдем искомое значение (afterNode)
        current = self.head
        while current is not None:
            if current.value == afterNode.value:
                break
            # Здесь мы присваеиваем текущему значение то которое лежало в указазателе
            current = current.next

        # Проверка на отсутствие элемента в списке
        if current is None:
            raise ValueError("node not in the list")
        else:
            # Проверка на соответствие типа элемента
            if type(newNode) == Node:
                new_node = newNode.value
            else:
                new_node = Node(newNode)

            # Переназначаем указатели у node списка. Сперва делаем указатель у нового элемента. Потом помещаем новый
            # элемент в указатель текущего.
            new_node.next = current.next
            current.next = new_node
        return
