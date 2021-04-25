import unittest
from src.rest_api.app import *

class Test(unittest.TestCase):
    def set_up(self):
        app.config ['TESTING'] = True
        app.config ['DEBUG'] = False
        self.app = app.client_test()
        
    def tear_down(self):
        pass
    
    def test(self):
        response = self.app.get('/', follow_redirects=True)
        self.asserEqual(response.status_code, 200)
      
if __name__ == ' __main__':
    unittest.main()
    
        
