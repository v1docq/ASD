from single_linked_list import Node, LinkedList
from func import sum_function


def get_linked_list(tail_flag: bool = False):
    node1 = Node(12)
    node2 = Node(99)
    node3 = Node(128)
    node4 = Node(32)
    s_list = LinkedList()
    s_list.add_in_tail(node1)
    s_list.add_in_tail(node2)
    s_list.add_in_tail(node3)
    s_list.add_in_tail(node4)
    if tail_flag:
        s_list.insert(afterNode=Node(128), newNode=99)
        s_list.insert(afterNode=Node(32), newNode=32)
        s_list.insert(afterNode=Node(32), newNode=32)
    return s_list


def test_delete_function():
    s_list = get_linked_list(tail_flag=True)
    len_before = s_list.len()
    s_list.delete(99, all=False)
    len_after_1_delete = s_list.len()
    s_list = get_linked_list(tail_flag=True)
    s_list.delete(99, all=True)
    len_after_2_delete = s_list.len()
    s_list = get_linked_list(tail_flag=True)
    s_list.delete(32, all=True)
    s_list.print_all_nodes()
    len_after_3_tail_delete = s_list.len()
    assert len_after_1_delete == len_before - 1
    assert len_after_2_delete == len_before - 2
    assert len_after_3_tail_delete == len_before - 3


def test_find_function(val: int = 99,
                       check_flag: bool = False
                       ):
    s_list = get_linked_list()
    tmp_list = s_list.find_all(val)
    for i in tmp_list:
        if i.value != val:
            check_flag = True
    assert type(tmp_list) == list
    assert not check_flag


def test_len_function():
    s_list = get_linked_list()
    assert s_list.len() == 5


def test_clean_function():
    s_list = get_linked_list()
    s_list.clean()
    assert s_list.len() == 0


def test_insert_function():
    s_list = get_linked_list()
    len_before = s_list.len()
    s_list.insert(afterNode=Node(37), newNode=155)
    len_after = s_list.len()
    assert len_after > len_before


def test_sum_func():
    f_list = get_linked_list()
    s_list = get_linked_list()
    sum_list = sum_function(f_list, s_list)
    assert sum_list.len() == f_list.len()
