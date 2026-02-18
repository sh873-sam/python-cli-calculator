import pytest
from app.operation.operations import add, subtract, multiply, divide


@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (-1, 1, 0), (2.5, 2.5, 5.0)])
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [(5, 2, 3), (0, 5, -5), (2.5, 1.0, 1.5)])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [(2, 3, 6), (-2, 3, -6), (2.5, 2, 5.0)])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [(6, 3, 2), (5, 2, 2.5), (-6, 3, -2)])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


def test_divide_by_zero_raises():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
