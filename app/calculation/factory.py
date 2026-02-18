from typing import Callable, Dict

from app.operation.operations import add, subtract, multiply, divide
from app.calculation.calculation import Calculation


class CalculationFactory:
    _ops: Dict[str, Callable[[float, float], float]] = {
        "add": add,
        "+": add,
        "subtract": subtract,
        "-": subtract,
        "multiply": multiply,
        "*": multiply,
        "divide": divide,
        "/": divide,
    }

    @classmethod
    def create(cls, operation_input: str, a: float, b: float) -> Calculation:
        op_key = operation_input.strip().lower()

        # EAFP: try; fail cleanly if missing
        try:
            operation = cls._ops[op_key]
        except KeyError as exc:
            raise ValueError(f"Unknown operation: '{operation_input}'.") from exc

        name_map = {"+": "add", "-": "subtract", "*": "multiply", "/": "divide"}
        operation_name = name_map.get(op_key, op_key)

        return Calculation(operation_name=operation_name, a=a, b=b, operation=operation)
