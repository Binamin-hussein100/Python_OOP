# import pytest

from calculator.operations import add,subtract
def test_add():
    assert add(2,3) == 5


def test_subtract():
    assert subtract(5,3) == 2

def stringify():
    assert f"Test"
    