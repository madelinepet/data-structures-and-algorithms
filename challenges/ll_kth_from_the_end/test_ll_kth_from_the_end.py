from .ll_kth_from_the_end import LinkedList
import ll_kth_from_the_end
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


def test_linked_list_exists():
    assert small_list


def test_create_instance_of_ll():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_default_property_head(empty_list):
    assert empty_list.head is None


def test_default_property_length(empty_list):
    assert empty_list._length == 0


def test_insert_successful(empty_list):
    assert empty_list.head is None
    empty_list.insert(25)
    assert empty_list.head.val == 25


def test_length_of_list_increases_on_insertion(empty_list):
    assert len(empty_list) == 0
    empty_list.insert(25)
    assert len(empty_list) == 1


def test_includes_returns_true_if_exists(small_list):
    actual = small_list.includes(4)
    assert actual is True
    assert small_list.includes(1) is True


def test_includes_returns_false_if_not_exists(small_list):
    assert small_list.includes(100) is False
    assert small_list.includes(0) is False


def test_insertion_of_iterable():
    ll = LinkedList([1, 2, 3])
    assert len(ll) == 3


def test_create_instance_non_iterable():
    ll = LinkedList(1)
    assert len(ll) == 1


def test_linked_list_append_exists():
    assert LinkedList.append


def test_append_after_places_new_node_at_end(small_list):
    """ Test if we added the value to the end of the list
    """
    a = 42
    expected = len(small_list) + 1
    small_list.append(a)
    actual = len(small_list)
    assert small_list.includes(a)
    assert expected == actual


def test_ll_kth_from_end_item_not_in_list(small_list):
    expected = 'Exemption'
    actual = ll_kth_from_the_end(5)
    assert expected == actual


def test_ll_kth_from_end_last_num(small_list):
    expected = 4
    actual = ll_kth_from_the_end(0)
    assert expected == actual


def test_ll_kth_from_end_item_first_num(small_list):
    expected = 1
    actual = ll_kth_from_the_end(3)
    assert expected == actual


def test_ll_kth_from_end_item_middle_num(small_list):
    expected = 3
    actual = ll_kth_from_the_end(1)
    assert expected == actual


def test_ll_kth_from_end_empty_list(empty_list):
    expexted = 'Exemption'
    actual = ll_kth_from_the_end(5)
    assert expexted == actual





