def flatten(list_in: list) -> list:
    """
    The func takes a list, containing list among another elements, and returns a one-level list
    Example: [[2], 5, [[2], [5, 4]]] -> [2, 5, 2, 5, 4]

    Parameters:
        list_in (list): list, that may contain lists among its elements
    Returns:
        result (list): one-leveled list
    """
    result = []
    for el in list_in:
        if isinstance(el, list):
            el = flatten(el)
            result += el
        else:
            result.append(el)

    return result
