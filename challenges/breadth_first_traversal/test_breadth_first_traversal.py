import pytest
from .breadth_first_traversal import BinaryTree


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
    tree.insert(1)
    return tree


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


def test_root_large_tree_value(large_tree):
    """ Root of large tree should be 11
    """
    assert large_tree.root.value == 11


def test_root_of_large_tree_left_val(large_tree):
    """ Test that left is 2
    """
    assert large_tree.root.left.value == 2


def test_root_of_large_tree_left__left_val(large_tree):
    """ Test that left and left again of root is 1
    """
    assert large_tree.root.left.left.value == 1


def test_root_of_large_tree_left_right_val(large_tree):
    """ Test that left and right again of root is 3
    """
    assert large_tree.root.left.right.value == 3


def test_root_of_large_tree_right_val(large_tree):
    """ Test that right of root is 12
    """
    assert large_tree.root.right.value == 12


def test_root_of_large_tree_right_right_val(large_tree):
    """ Test that right and right again of root is 44
    """
    assert large_tree.root.right.right.value == 44


def test_root_of_large_tree_right_right_left_val(large_tree):
    """ Test that right and right and then left of root is 27
    """
    assert large_tree.root.right.right.left.value == 27


def test_root_left_left_left_none(large_tree):
    """ Test no node left, left, left of root
    """
    assert large_tree.root.left.left.left is None


def test_root_left_left_right_none(large_tree):
    """ Test no node left, left, right of root
    """
    assert large_tree.root.left.left.right is None


def test_root_left_right_left_none(large_tree):
    """ Test no node left, right, left of root
    """
    assert large_tree.root.left.right.left is None


def test_root_right_left_none(large_tree):
    """ Test no node right and left of root
    """
    assert large_tree.root.right.left is None


def test_root_right_right_left_left_none(large_tree):
    """ Test no node right, right, left, left of root
    """
    assert large_tree.root.right.right.left.left is None


def test_empty_bt():
    bt = BinaryTree()
    assert isinstance(bt, BinaryTree)
    assert bt.root is None


def test_insert_into_empty_bt():
    bt = BinaryTree()
    assert bt.root is None
    bt.insert(25)
    assert bt.root.value == 25


def test_iterable_creates_bt():
    bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    assert bt.root.value == 20
    assert bt.root.left.value == 18
    assert bt.root.right.value == 40


def test_inorder_traversal():
    bt = BinaryTree([20, 18, 12, 19, 11, 14, 40, 31, 22, 33])
    expected = [11, 12, 14, 18, 19, 20, 22, 31, 33, 40]
    actual = []

    def generate_list(node):
        actual.append(node.value)
    bt.in_order(generate_list)
    assert expected == actual
