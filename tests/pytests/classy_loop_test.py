import pytest
from src.classy_calc import *

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

'''    
@pytest.mark.parametrize("test_input, expected", [(1,5)])
def choice_test(test_input, expected):
    assert choice(test_input) == expected
''' 
 
def test_main_choice_loop():
    assert main(1) == print(calculator.addition())
    
    
