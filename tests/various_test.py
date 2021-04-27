import unittest
from test import support

from src.rest_api import *

class MyTest(TestCase):

    def create_app(self):
        return myflaskapp

    def test_greeting(self):
        self.app.get('/')
        self.assert_template_used('app.html')
        
if __name__ == '__main__':
    unittest.main()
