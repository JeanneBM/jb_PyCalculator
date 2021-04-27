from src.if_loop import *

def test_add(capsys):
  
    while True:
      # try
      choice = 1
      x = 3.0
      y = 2.0

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
