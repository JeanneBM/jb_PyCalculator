import pytest
from src.classy_calc import PyCalculator

x = 3.0
y = 2.0

@pytest.fixture
def calculator():
    return PyCalculator(x,y)

def verify_answer(expected, answer):
    assert expected == answer

def test_add(calculator):
    answer = calculator.addition()
    verify_answer(5.0, answer)


def test_subtract(calculator):
    answer = calculator.subtraction()
    verify_answer(1.0, answer)


def test_multiply(calculator):
    answer = calculator.multiplication()
    verify_answer(6.0, answer)


def test_division(calculator):
    answer = calculator.divi()
    verify_answer(1.5, answer)




    
    
