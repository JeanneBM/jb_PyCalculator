import pytest
from src.classy_calc import PyCalculator

x = 3.0
y = 0.0

@pytest.fixture
def calculator():
    return PyCalculator(x,y)

def verify_answer(expected, answer):
    assert expected == answer

def test_division(calculator):
    answer = calculator.division()
    verify_answer("Division by zero. We cannot perform this operation.", answer)
