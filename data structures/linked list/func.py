# Напишите функцию, которая получает на вход два связанных списка, состоящие из целых значений,
# и если их длины равны, возвращает список, каждый элемент которого равен сумме соответствующих элементов входных списков.

from LinkedList import LinkedList, Node


def sum_function(first_list: LinkedList, second_list: LinkedList):
    if first_list.len() != second_list.len():
        raise ValueError('Please specify two equal Linked Lists')
    else:
        if first_list.head and second_list.head is None:
            return LinkedList()
        node_list = []
        sum_list = LinkedList()
        node = first_list.head
        second_node = second_list.head
        while node is not None:
            new_val = node.value + second_node.value
            node = node.next
            second_node = second_node.next
            node_list.append(Node(new_val))
        for elem in node_list:
            sum_list.add_in_tail(elem)
        return sum_list
