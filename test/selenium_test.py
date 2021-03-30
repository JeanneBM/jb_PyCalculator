'''
from selenium import webdriver


class WebApp:
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = WebApp()
        return cls.instance
    
    

webapp = WebApp.get_instance()
'''
