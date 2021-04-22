import pytest
from src.classy_calc import *

x = 3.0
y = 2.0

@pytest.fixture
def calculator1():
    return PyCalculator(x,y)

def verify_answer(expected, answer):
    assert expected == answer

def test_add(calculator1):
    answer = calculator1.addition()
    verify_answer(5.0, answer)

'''    
@pytest.mark.parametrize("test_input, expected", [(1,5)])
def choice_test(test_input, expected):
    assert choice(test_input) == expected
''' 
def main_test():
    return main(choice, x,y)

def test_loop(main_test):
    assert choice(1) == print(calculator.addition())
    
    
