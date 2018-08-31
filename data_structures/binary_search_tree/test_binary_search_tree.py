import pytest
from .binary_search_tree import BinaryTree


@pytest.fixture
def small_tree():
    tree = BinaryTree()
    tree.insert(3)
    tree.insert(11)
    tree.insert(27)
    return tree


@pytest.fixture
def large_tree():
    tree = BinaryTree()
    tree.insert(11)
    tree.insert(2)
    tree.insert(3)
    tree.insert(12)
    tree.insert(44)
    tree.insert(27)


def test_root_val(small_tree):
    """ Test that small tree has a root
    """
    assert small_tree.root.value == 3


def test_root_of_small_tree_has_left_child(small_tree):
    """ Tests that there is no left child of small list
    """
    assert small_tree.root.left is None


def test_root_of_small_tree_has_right_child(small_tree):
    """ Test that root of small tree has a rihjy child
    """
    assert small_tree.root.right.value == 11


def test_root_of_small_tree_has_a_right_child_with_a_right_child(small_tree):
    """ Test that right child of root has right child
    """
    assert small_tree.root.right.right.value == 27


