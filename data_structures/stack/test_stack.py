from .stack import Stack

import pytest


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def small_stack():
    stack = Stack()
    stack.insert(1)
    stack.insert(2)
    stack.insert(3)
    stack.insert(4)
    return stack


def test_stack_exists():
    assert small_stack


def test_create_instance_of_stack():
    stack = Stack()
    assert isinstance(stack, Stack)


def test_default_property_top(empty_stack):
    assert empty_stack.top is None


def test_default_property_length(empty_stack):
    assert empty_stack._length == 0


def test_insert_successful(empty_stack):
    assert empty_stack.top is None
    empty_stack.push(25)
    assert empty_stack.top.val == 25


def test_length_of_stack_increases_on_insertion(empty_stack):
    assert len(empty_stack) == 0
    empty_stack.push(25)
    assert len(empty_stack) == 1


def test_length_of_stack_decreases_on_pop(empty_stack):
    assert len(empty_stack) == 0
    empty_stack.push(25)
    empty_stack.push(30)
    empty_stack.pop()
    assert len(empty_stack) == 1
