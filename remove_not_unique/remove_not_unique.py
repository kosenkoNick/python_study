from collections.abc import Iterable


def remove_not_unique(list_in: list[int]) -> Iterable[int]:
    """
    This method takes an iterable of integers and removes values, that have one appearance
    Parameters:
        list_in (list[int]): list of int values
    Returns:
        list_in (list[int]): list without unique elems
    """
    for val in set(list_in):
        if list_in.count(val) == 1:
            list_in.remove(val)
    return list_in


def test_check1():
    test_list = [1, 2, 1, 2, 1, 2, 3]
    assert remove_not_unique(test_list) == [1, 2, 1, 2, 1, 2]


def test_check2():
    test_list = [1, 2, 3, 4, 5, 6]
    assert remove_not_unique(test_list) == []


def test_check3():
    test_list = [1, 1, 2, 2, 3, 3]
    assert remove_not_unique(test_list) == [1, 1, 2, 2, 3, 3]
