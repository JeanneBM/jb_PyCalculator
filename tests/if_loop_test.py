import unittest
from test import support

from src.rest_api import app

class MyTest(unittest.TestCase):

    def setUp(self):
        self.app.config['TESTING'] = True
        self.app.config['DEBUG'] = False
        self.app = app.test_client()
        
    def create_app(self):
        return app

    def test_greeting(self):
        self.app.get('/')
        self.assert_template_used('app.html')
        
if __name__ == '__main__':
    unittest.main()
