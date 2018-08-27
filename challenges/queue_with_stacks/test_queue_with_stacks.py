from queue_with_stacks import (Node, Stack, Queue)

import pytest


@pytest.fixture
def empty_stack():
    return Stack()


@pytest.fixture
def empty_stack_two():
    return Stack()


@pytest.fixture
def small_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    return stack


@pytest.fixture
def empty_queue():
    return Queue()


@pytest.fixture
def small_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    return queue


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


def test_queue_exists():
    assert small_queue


def test_create_instance_of_queue():
    queue = Queue()
    assert isinstance(queue, Queue)


def test_default_property_front(empty_queue):
    assert empty_queue.front is None


def test_default_property_back(empty_queue):
    assert empty_queue.back is None


def test_length_of_queue_increases_on_insertion(empty_queue):
    empty_queue.enqueue(25)
    assert empty_queue._length == 1


def test_length_of_queue_decreases_on_pop(empty_queue):
    assert len(empty_queue) == 0
    empty_queue.enqueue(25)
    empty_queue.enqueue(30)
    empty_queue.dequeue()
    assert empty_queue._length == 1


