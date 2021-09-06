from LinkedList import Node, LinkedList
from func import sum_function


def get_linked_list():
    node1 = Node(12)
    node2 = Node(99)
    node3 = 37
    node1.next = node2
    node2.next = node3
    s_list = LinkedList()
    s_list.add_in_tail(node1)
    s_list.add_in_tail(node2)
    s_list.add_in_tail(Node(128))
    s_list.insert(afterNode=Node(128), newNode=37)
    s_list.insert(afterNode=Node(37), newNode=99)
    return s_list


def test_delete_function():
    s_list = get_linked_list()
    len_before = s_list.len()
    s_list.delete(128)
    s_list.delete(99, all=True)
    len_after = s_list.len()
    assert len_after < len_before


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

