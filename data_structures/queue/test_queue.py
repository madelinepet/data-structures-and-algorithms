from .queue import Queue

import pytest


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


def test_queue_exists():
    assert small_queue


def test_create_instance_of_queue():
    queue = Queue()
    assert isinstance(queue, Queue)


def test_default_property_front(empty_queue):
    assert empty_queue.front is None


def test_default_property_back(empty_queue):
    assert empty_queue.back is None


def test_default_property_length(empty_queue):
    assert empty_queue._length == 0

