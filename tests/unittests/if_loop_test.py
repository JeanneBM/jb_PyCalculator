import unittest
from src.if_loop import addition

def test_add():
  assert addition((3,2)) == 5

if __name__ == "__main__":
  test_add()
  print("Everything passed")
