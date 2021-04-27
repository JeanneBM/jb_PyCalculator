import unittest
from src.if_loop import *

def test_add(capsys):
  

    # try
    choice = 1
    x = 3
    y = 2

    # when
    addition(x, y)
    out, err = capsys.readouterr()

    # then
    assert out == 'Select please one of the following operations:\n'
  
'''
if __name__ == "__main__":
  test_add()
  print("Everything passed")
'''
