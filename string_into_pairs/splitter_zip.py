from typing import Iterable


def split_pairs(string: str) -> Iterable[str]:
    """
    | Method splits given string into pairs. If string length is odd - it adds '_' symbol. It uses zip() to make pairs -
    | it zips every second char, beginning from the 0th and 1st index in string
    |
    | It adds the '_' everytime to the second iterable, look at the examples:
    - 'abcdef' -> zip('ace', 'bdf_') -> ['ab', 'cd', 'ef'] - len(string) is even, so zip will make 3 pairs, '_' is redundant
    - 'abcdef' -> zip('ace', 'bd_') -> ['ab', 'cd', 'e_']  - len(string) is odd, so '_' will make lengths equal, and it will be used

    :param string: string to split
    :return: iterable of strings
    """
    return [ch1 + ch2 for ch1, ch2 in zip(string[::2], string[1::2] + '_')]


print(split_pairs('abcdef'))
