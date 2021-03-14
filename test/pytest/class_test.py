import pytest
from ClassyCalc import PyCalculator

# "Constants"
x = 3.0
y = 2.0


# Fixtures

@pytest.fixture
def calculator():
    return PyCalculator()


# Helpers

def verify_answer(expected, answer, last_answer):
    assert expected == answer
    assert expected == last_answer


# Test Cases

def test_last_answer_init(calculator):
    assert calculator.last_answer == 0.0


def test_add(calculator):
    answer = calculator.addition(x, y)
    verify_answer(5.0, answer, calculator.last_answer)


def test_subtract(calculator):
    answer = calculator.subtraction(x, y)
    verify_answer(1.0, answer, calculator.last_answer)


def test_subtract_negative(calculator):
    answer = calculator.subtraction(x, y)
    verify_answer(-1.0, answer, calculator.last_answer)


def test_multiply(calculator):
    answer = calculator.multiplication(x, y)
    verify_answer(6.0, answer, calculator.last_answer)


def test_divide(calculator):
    answer = calculator.divide(x, y)
    verify_answer(1.5, answer, calculator.last_answer)


def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError) as e:
        calculator.division(x, 0)
    assert "Division by zero. We cannot perform this operation." in str(e.value)


    
    
