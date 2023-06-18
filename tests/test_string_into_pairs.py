import pytest
from string_into_pairs.splitter_range import split_pairs as range_split
from string_into_pairs.splitter_zip import split_pairs as zip_splitter


@pytest.mark.parametrize("func", [
        range_split, zip_splitter
])
@pytest.mark.parametrize("string, expected", [
    ('a', ['a_']),      # one letter
    ('', []),          # empty string
    ('abcdefe', ['ab', 'cd', 'ef', 'e_']),  # odd length
    ('abcdef', ['ab', 'cd', 'ef'])         # even length
])
def test_splitter(func, string, expected):
    assert func(string) == expected
