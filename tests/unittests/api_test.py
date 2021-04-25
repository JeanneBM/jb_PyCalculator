import unittest
from flask import Flask
from flask import render_template
from flask.ext.testing import TestCase
   
from src.rest_api.app import *

BASE_URL = 'http://localhost:5000/api/'


class Test(TestCase):
    def create_app(self):
        return myapp
    
    def tear_down(self):
        pass
    
    def web_test(self):
        self.app.get('/')
        self.assert_template_used('app.html')    
    
    def tear_down(self):
        pass
      
if __name__ == ' __main__':
    unittest.main()
    
        
