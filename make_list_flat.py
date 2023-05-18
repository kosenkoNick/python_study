def flattern(data : list) -> list:
    '''
    The func takes a list, containing list among aother elements, 
    and returns a one-level list
    Example: [[2], 5, [[2], [5, 4]]] -> [2, 5, 2, 5, 4]
    '''
    result = []
    for el in data:
        if isinstance(el, list):
            el = flattern(el)
            result += el
        else:
            result.append(el)

    return result
