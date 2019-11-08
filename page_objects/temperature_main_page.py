"""
This class models the main Temperature page.
"""
from .Base_Page import Base_Page
from .temperature_object import Temperature_Object
from utils.Wrapit import Wrapit


class Temperature_Main_Page(Base_Page,Temperature_Object):
    "Page Object for the temperature main page"
    
    def start(self):    
        "Use this method to go to specific URL -- if needed"
        url = ''
        self.open(url)
