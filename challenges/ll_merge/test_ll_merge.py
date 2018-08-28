from .ll_merge import LinkedList
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def empty_list_two():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll


@pytest.fixture
def small_list_two():
    ll = LinkedList()
    ll.insert(a)
    ll.insert(b)
    ll.insert(c)
    ll.insert(d)
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
    expected = len(small_list)
    small_list.append(a)
    actual = len(small_list)
    assert small_list.includes(a)
    assert expected == actual


def test_linked_list_append_insert_before():
    """ tests fn insert before exists
    """
    assert LinkedList.insert_before


def test_linked_list_append_insert_after():
    """ test insert_after exists
    """
    assert LinkedList.insert_after


def test_linked_list_merge_returns_not_valid_list(empty_list, empty_list_two):
    """ assert empty lists give back None
    """
    expected = None
    actual = LinkedList.ll_merge(empty_list, empty_list_two)
    assert expected == actual


def test_linked_list_merge_merges_lists_equal_lengths(small_list, empty_list):
    """ Test empty list and list input gives back list
    """
    expected = small_list
    actual = LinkedList.ll_merge(small_list, empty_list)
    assert expected == actual


def test_linked_list_merge_merges_lists_equal_lengths_other(small_list, empty_list):
    """ Test empty list and list input gives back list
    """
    expected = small_list
    actual = LinkedList.ll_merge(empty_list, small_list)
    assert expected == actual


def test_linked_list_ll_merge_exists():
    """ Test ll_merge exists
    """
    assert LinkedList.ll_merge



