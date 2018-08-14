from .array_shift import insert_shift_array
import pytest


def test_insert_shift_array_exists():
    assert insert_shift_array


def test_value_gets_added():
    expected = [1, 2, 3, 4, 5]
    actual = insert_shift_array([1, 2, 4, 5], 3)
    assert expected == actual


def test_list_can_add_strings():
    expected = [1, 2, 'a', 4, 5]
    actual = insert_shift_array([1, 2, 4, 5], 'a')
    assert expected == actual

