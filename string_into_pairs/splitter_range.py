from typing import Iterable


def split_pairs(string: str) -> Iterable[str]:
    """
    Method splits given string into pairs. If string length is odd - it adds '_' symbol
    :param string: string to split
    :return: iterable of strings
    """

    string += '_' if len(string) % 2 == 1 else ''
    return [str(string[i:i + 2]) for i in range(0, len(string), 2)]
