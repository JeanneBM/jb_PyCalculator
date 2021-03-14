import unittest

from src.classy_calc import PyCalculator

class unittest_pycalculator(unittest.TestCase):
  
  def setUp(self):
    self.calculator = PyCalculator()

  def test_add(self):
    self.assertEqual(self.calculator.addition(4,7), 11)  
    
  def test_subtract(self):
    self.assertEqual(self.calculator.subtraction(10,5), 5)  
    
  def test_multiply(self):
    self.assertEqual(self.calculator.multiplication(3,7), 21) 
    
  def test_divide(self):
    self.assertEqual(self.calculator.division(10,2), 5)
    
if __name__ == "__main__":
  unittest.main()
  
  
