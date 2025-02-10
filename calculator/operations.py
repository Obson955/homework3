"""Basic arithmetic operations module."""

from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Add two numbers."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Subtract two numbers."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Multiply two numbers."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Divide two numbers (no zero-division handling)."""
    return a / b
