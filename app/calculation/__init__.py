# Author: Edanur Sasmaz
#Date: Sept 29,2025
# calculator_calculations.py

from abc import ABC, abstractmethod
from app.operation import Operation

class Calculation(ABC):
    def __init__(self, a: float, b: float) -> None:
        self.a = a
        self.b = b

    @abstractmethod
    def execute(self) -> float:
        ...

    def __str__(self) -> str:
        result = self.execute()
        op_name = self.__class__.__name__.replace("Calculation", "")
        return f"{self.__class__.__name__}: {self.a} {op_name} {self.b} = {result}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(a={self.a}, b={self.b})"


class CalculationFactory:
    _calculations = {}

    @classmethod
    def register_calculation(cls, calculation_type: str):
        def decorator(subclass):
            key = calculation_type.lower()
            if key in cls._calculations:
                raise ValueError(f"Calculation type '{calculation_type}' is already registered.")
            cls._calculations[key] = subclass
            return subclass
        return decorator

    @classmethod
    def create_calculation(cls, calculation_type: str, a: float, b: float) -> Calculation:
        key = calculation_type.lower()
        calculation_class = cls._calculations.get(key)
        if not calculation_class:
            available = ", ".join(cls._calculations.keys())
            raise ValueError(f"Unsupported calculation type: '{calculation_type}'. Available types: {available}")
        return calculation_class(a, b)


@CalculationFactory.register_calculation("add")
class AddCalculation(Calculation):
    def execute(self) -> float:
        return Operation.addition(self.a, self.b)


@CalculationFactory.register_calculation("subtract")
class SubtractCalculation(Calculation):
    def execute(self) -> float:
        return Operation.subtraction(self.a, self.b)


@CalculationFactory.register_calculation("multiply")
class MultiplyCalculation(Calculation):
    def execute(self) -> float:
        return Operation.multiplication(self.a, self.b)


@CalculationFactory.register_calculation("divide")
class DivideCalculation(Calculation):
    def execute(self) -> float:
        if self.b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return Operation.division(self.a, self.b)