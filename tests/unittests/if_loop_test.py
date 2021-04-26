import unittest
from src.if_loop import *

def test_add():
  
  x = 3.0
  y = 2.0

 
  result = addition(x, y)
  
  assert result
  assert addition(4,5)
    
if __name__ == "__main__":
    test_add()
    print("Everything passed")
