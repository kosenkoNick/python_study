import pytest
from string_into_pairs.splitter import split_pairs


@pytest.mark.parametrize("string, expected", [
    ('a', ['a_']),      # one letter
    ('', []),          # empty string
    ('abcdefe', ['ab', 'cd', 'ef', 'e_']),  # odd length
    ('abcdef', ['ab', 'cd', 'ef'])         # even length
])
def test_splitter(string, expected):
    assert split_pairs(string) == expected
