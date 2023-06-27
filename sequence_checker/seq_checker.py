def goes_after(word: str, first: str, second: str) -> bool:
    """
    Method checks if one symbol goes right after another in the given word
    Parameters:
        word (str): the given word
        first (str): first symbol
        second (str): second symbol
    Returns:
        (bool): True/False, depending on the symbols order
    """
    if first not in word or second not in word or second == first:
        return False
    elif word.index(second) - word.find(first) == 1:
        return True
    else:
        return False


def test_general_tests():
    assert goes_after("world", "w", "o") is True
    assert goes_after("world", "w", "r") is False
    assert goes_after("world", "l", "o") is False
    assert goes_after("panorama", "a", "n") is True
    assert goes_after("list", "l", "o") is False
    assert goes_after("", "l", "o") is False
    assert goes_after("list", "l", "l") is False
    assert goes_after("world", "d", "w") is False
    assert goes_after("Almaz", "a", "l") is False
