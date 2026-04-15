import pytest
from math_utils import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, -2, -3),
    (0, 5, 5),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected