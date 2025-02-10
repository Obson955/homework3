"""Test suite for the Calculation class."""

from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add, subtract

def test_calculation_add():
    """Test performing an addition calculation."""
    calc = Calculation(Decimal('1.0'), Decimal('2.0'), add)
    assert calc.perform() == Decimal('3.0')

def test_calculation_subtract():
    """Test performing a subtraction calculation."""
    calc = Calculation(Decimal('5.0'), Decimal('3.0'), subtract)
    assert calc.perform() == Decimal('2.0')
