import unittest
from test import support

from src.rest_api import *

class MyTest(unittest.TestCase):

    def create_app(self):
        return app

    def test_greeting(self):
        self.app.get('/')
        self.assert_template_used('app.html')
        
if __name__ == '__main__':
    unittest.main()
