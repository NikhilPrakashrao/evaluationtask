"""
This class models the form on the weather shopper application main page
"""

from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit


class Temperature_Object:
    "Page object for the temperature page"    
    #locators
    temp_field = locators.temp_field
    click_buy_moisturizers = locators.click_moisturizers
    click_buy_sunscreens = locators.click_sunscreens
    redirect_title_mositurizers = 'moisturizers'
    redirect_title_sunscreens = 'sunscreens'

    

    def get_temperature(self):
        "get the temperature value from the page"
        temp_element = self.get_element(self.temp_field).text
        temp_element = temp_element[:-2]     

        return temp_element

    def click_moisturizers(self):
        "click the Buy moisturizers button"      
        result_flag = self.click_element(self.click_buy_moisturizers)
        self.conditional_write(result_flag,
            positive='Clicked on the "Buy moisturizers" button',
            negative='Failed to click on "Buy moisturizers" button',
            level='debug')

        return result_flag

    def click_sunscreens(self):
        "click the Buy sunscreens button"
        result_flag = self.click_element(self.click_buy_sunscreens)
        self.conditional_write(result_flag,
            positive='Clicked on the "Buy sunscreens" button',
            negative='Failed to click on "Buy sunscreens" button',
            level='debug')

        return result_flag

    def check_redirect_moisturizers(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False       
        if self.redirect_title_mositurizers in self.driver.title.lower():
            self.switch_page('moisturizers') ## added switch_page statement
            result_flag = True ##False changed to true
            
        
        return result_flag    

    def check_redirect_sunscreens(self):
        "Check if we have been redirected to the redirect page"
        result_flag = False       
        if self.redirect_title_sunscreens in self.driver.title.lower():## added lower
            self.switch_page('sunscreens')   ## added switch_page statement
            result_flag = True ##False changed to true 
            
            return result_flag

    def process_temperature(self):
        "check the temperature"
        result_flag = False
        temp_element = self.get_temperature()
        if int(temp_element) <=19: ## added int
            result_flag = self.click_moisturizers() ##removed self from brackets
            result_flag &= self.check_redirect_moisturizers() ##removed self from brackets
        elif int(temp_element) >=34: ## added int
            result_flag = self.click_sunscreens()  ##removed self from brackets          
            result_flag &= self.check_redirect_sunscreens() ##removed self from brackets
        
        return result_flag