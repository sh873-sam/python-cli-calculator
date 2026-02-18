from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Calculation:
    operation_name: str
    a: float
    b: float
    operation: Callable[[float, float], float]

    def compute(self) -> float:
        return self.operation(self.a, self.b)

    def __str__(self) -> str:
        return f"{self.operation_name}({self.a}, {self.b})"
