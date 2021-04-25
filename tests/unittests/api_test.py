import unittest
from flask import Flask
from flask import render_template
from src.rest_api.app import *

BASE_URL = 'http://localhost:5000/api/'

class Test(unittest.TestCase):
    def create_app(cfg=None):
        app = Flask(__name__)
        app.config['DEBUG'] = True
        app.config['TESTING'] = True
        return app
        
    def tear_down(self):
        pass
    
    def flask_application_is_up_and_running_test(self):
        response = urllib2.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200) 
    
    def web_test(self):
        self.app.get('/')
        self.assert_template_used('app.html')
      
if __name__ == ' __main__':
    unittest.main()
    
        
