import unittest
from src.classy_calc import PyCalculator

x = -10.0
y = -2.0


class class_unittest(unittest.TestCase):


    def test_division(self):
        self.assertEqual(self.calculator.division(),-5)


if __name__ == "__main__":
    unittest.main()
