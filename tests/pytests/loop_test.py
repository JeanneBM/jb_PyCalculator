import pytest
from src.classy_calc import *

#choice = str(1)

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


def test_main():
    assert choice(1) == test_add.answer

