def flatten(list_in: list) -> list:
    """
    The func takes a list, containing list among another elements, and returns a one-level list
    Example: [[2], 5, [[2], [5, 4]]] -> [2, 5, 2, 5, 4]

    Parameters:
        list_in (list): list, that may contain lists among its elements
    Returns:
        result (list): one-leveled list
    """
    import re
    result = [int(val) for val in re.sub('(\[)|(])|(,)', '', str(list_in)).split(' ')]

    return result


def test_check1():
    test_list = [[2], 5, [[2], [5, 4]]]

    result_list = flatten(test_list)

    assert result_list == [2, 5, 2, 5, 4]
    assert len(result_list) == 5


def test_check2():
    test_list = [2, 5, 2, 5, 4]
    assert flatten(test_list) == test_list
