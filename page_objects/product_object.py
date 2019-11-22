"""
This class models the form on the weather shopper application Moisturizer/Sunscreen product page
"""
from selenium import webdriver
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import re

class Product_Object:
    "Page object for the Moisturizer and sunscreens"     
    #locators  
    product_price_element = locators.product_price_element
    product_add_element = locators.product_add_element
    cart_button = locators.click_cart  
    checkout_heading = locators.checkout_heading
    sunscreen_heading = locators.heading_sunscreen
    moisturizers_heading = locators.heading_moisturizer    
    product_category = []    
    product_moisturizers_category = []
    product_sunscreens_category = []
    

    def add_products(self,product_category):
        "Add products to the cart"       
        result_flag = False   
        for product in product_category:
            price_product = 100000          
            product_elements = self.get_elements(self.product_price_element%product)            
            for element in product_elements:                           
                product_price = element.text                                   
                product_price = re.findall(r'\b\d+\b', product_price)                        
                if int(product_price[0]) < price_product:                   
                    price_product = int(product_price[0])                               
                    result_flag = self.click_element(self.product_add_element%(product,price_product)) #Moving inside if
            self.conditional_write(result_flag,
                                positive='Successfully added products',
                                negative='Failed to add products',
                                level='debug')        

        return result_flag

    def click_cart(self):
        "Click on the Cart button"
        result_flag = self.click_element(self.cart_button)
        self.conditional_write(result_flag,
            positive='Clicked on the "cart" button',
            negative='Failed to click on "cart" button',
            level='debug')

        return result_flag ## Added return statement  


    def process_selected_products(self,product_category):
        "Process the selected products"        
        result_flag = self.add_products(product_category)
        result_flag &= self.click_cart()
       
        return result_flag

    def select_product_type(self,product_moisturizers_category,product_sunscreens_category):
        "Select products type"          
        result_flag = False
        if 'sunscreen' in self.get_current_url():
            result_flag = self.process_selected_products(product_sunscreens_category)            
        else:           
            result_flag = self.process_selected_products(product_moisturizers_category)  ## changed sunscreens to moisturizers            
        
        return result_flag  

