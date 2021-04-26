import unittest
from src.if_loop import *

x = 3.0
y = 2.0


class class_unittest(unittest.TestCase):

    def setUp(self):
        self.calculator = PyCalculator(x,y)
'''
    def test_add(self):
        self.assertEqual(self.calculator.addition(),5)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtraction(),1)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(),6)

    def test_division(self):
        self.assertEqual(self.calculator.division(),1.5)

'''

    def verify_answer(expected, answer):
        assert expected == answer
        
    def add_test(calculator):
        answer = calculator.add(x, y)
        verify_answer(5.0, answer)
        
        
if __name__ == "__main__":
    unittest.main()
        
        
