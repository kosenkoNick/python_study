import pytest

from make_list_flat.flattener__recursive import flatten as flatten_recursive
from make_list_flat.flattener__regex import flatten as flatten_re


@pytest.mark.parametrize("func", [
    flatten_recursive,
    flatten_re
])
@pytest.mark.parametrize("data, expected", [
    ([2, 3, 4, 5, 6], [2, 3, 4, 5, 6]),  # already flat will return flat
    ([[2], 3], [2, 3]),     # multilayer to flat
])
def test_check_parametrize(func, data, expected):
    assert func(data) == expected
