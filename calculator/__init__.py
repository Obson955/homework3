"""Basic Calculator class with arithmetic operations."""

from decimal import Decimal
from calculator.operations import add, subtract, multiply, divide

class Calculator:
    """A simple calculator without history tracking."""

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Add two numbers."""
        return add(a, b)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Subtract two numbers."""
        return subtract(a, b)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Multiply two numbers."""
        return multiply(a, b)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Divide two numbers."""
        return divide(a, b)
