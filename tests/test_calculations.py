import pytest
from app.calculation.factory import CalculationFactory


def test_calculation_compute_add():
    calc = CalculationFactory.create("add", 1, 2)
    assert calc.compute() == 3


@pytest.mark.parametrize(
    "op,a,b,expected",
    [
        ("+", 1, 2, 3),
        ("-", 5, 2, 3),
        ("*", 2, 4, 8),
        ("/", 8, 2, 4),
        ("multiply", 3, 3, 9),
    ],
)
def test_factory_operations(op, a, b, expected):
    calc = CalculationFactory.create(op, a, b)
    assert calc.compute() == expected


def test_factory_invalid_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("nope", 1, 2)
def test_calculation_str():
    calc = CalculationFactory.create("add", 1, 2)
    assert str(calc) == "add(1, 2)"
