"""Basic Calculation module for arithmetic operations."""

from decimal import Decimal
from typing import Callable

class Calculation:
    """Represents a basic calculation with two operands and an operation."""

    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Initialize a Calculation with two operands and an operation."""
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> Decimal:
        """Perform the calculation and return the result."""
        return self.operation(self.a, self.b)
