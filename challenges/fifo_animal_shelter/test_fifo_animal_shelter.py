from .fifo_animal_shelter import AnimalShelter

import pytest


@pytest.fixture
def empty_queue():
    return AnimalShelter()


@pytest.fixture
def small_queue():
    queue = AnimalShelter()
    queue.enqueue('cat')
    queue.enqueue('dog')
    queue.enqueue('cat')
    queue.enqueue('cat')
    return queue


def test_queue_exists():
    assert small_queue


def test_create_instance_of_queue():
    queue = AnimalShelter()
    assert isinstance(queue, AnimalShelter)


def test_default_property_front(empty_queue):
    assert empty_queue.front is None


def test_default_property_back(empty_queue):
    assert empty_queue.back is None


def test_length_of_queue_increases_on_insertion(empty_queue):
    empty_queue.enqueue(25)
    assert empty_queue._length == 1


def test_length_of_queue_decreases_on_pop(empty_queue):
    assert empty_queue._length == 0
    empty_queue.enqueue('cat')
    empty_queue.enqueue('dog')
    empty_queue.dequeue()
    assert empty_queue._length == 1


def test_cant_add_non_dog_cat(empty_queue):
    expected = None
    actual = AnimalShelter.enqueue(empty_queue, 'birb')
    assert expected == actual
