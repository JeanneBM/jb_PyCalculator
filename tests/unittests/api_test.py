import unittest
#from flask import Flask
#from flask import render_template
from src.rest_api.app import *

BASE_URL = 'http://localhost:5000/api/'

class Test(unittest.TestCase):
    def create_app(cfg=None):
        app = Flask(__name__)
        return app
        
    def tear_down(self):
        pass
    
    def web_test(self):
        self.app.get('/')
        self.assert_template_used('app.html')
      
if __name__ == ' __main__':
    unittest.main()
    
        
