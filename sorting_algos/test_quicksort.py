import pytest
from .quicksort import quicksort


def test_gets_sorted():
    """ Happy path test making sure an unsorted list becomes sorted
    """
    unsorted = [3, 2, 1, 4]
    assert quicksort(unsorted, 0, 3) == [1, 2, 3, 4]


def test_non_list_throws_error():
    """ Tests to make sure an input str throws an error
    """
    unsorted = 'a,b,c,d'
    with pytest.raises(TypeError):
        quicksort(unsorted, 0, 3)


def test_doesnt_mess_up_already_sorted():
    """ Tests to make sure an already sorted list remains the same
    """
    unsorted = [num for num in range(20)]
    now_sorted = quicksort(unsorted, 0, 19)
    assert unsorted == now_sorted


def test_sorts_list_of_duplicates():
    """ Tests a list with duplicates to make sure it gets sorted
    """
    unsorted = [4, 4, 5, 3, 2, 3, 4, 3, 4, 5]
    expected = [2, 3, 3, 3, 4, 4, 4, 4, 5, 5]
    now_sorted = quicksort(unsorted, 0, 9)
    assert expected == now_sorted
