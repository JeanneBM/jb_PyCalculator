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
    assert out == '5\n'
  
'''
if __name__ == "__main__":
  test_add()
  print("Everything passed")
'''
