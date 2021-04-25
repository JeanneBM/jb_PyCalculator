import unittest
from src.rest_api.app import *

BASE_URL = 'http://localhost:5000/api/'

class Test(unittest.TestCase):
    def setup(self):
        app.config ['TESTING'] = True
        app.config ['DEBUG'] = False
        self.app = app.client_test()
        
    def tear_down(self):
        pass
    
    def web_test(self):
        self.app.get('/')
        self.assert_template_used('app.html')
      
if __name__ == ' __main__':
    unittest.main()
    
        
