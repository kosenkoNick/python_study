from typing import Iterable


def split_pairs(string: str) -> Iterable[str]:
    """
    Method splits given string into pairs. If string length is odd - it adds '_' symbol
    :param string: string to split
    :return: iterable of strings
    """
    if len(string) % 2 == 1:
        string += '_'

    return [str(string[i:i+2]) for i in range(0, len(string), 2)]


assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]

