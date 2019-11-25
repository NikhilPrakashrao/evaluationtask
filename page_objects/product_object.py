"""
This class models the form on the weather shopper application Moisturizer/Sunscreen product page
"""
from selenium import webdriver
from .Base_Page import Base_Page
import conf.locators_conf as locators
from utils.Wrapit import Wrapit
import re
import random
import time

class Product_Object:
    "Page object for the Moisturizer and sunscreens"     
    #locators  
    product_price_element = locators.product_price_element
    product_add_element = locators.product_add_element
    cart_button = locators.click_cart  
    pay_with_card = locators.pay_with_card
    iframe_name = locators.iframe_name
    email = locators.email
    card_number = locators.card_number
    card_expiry = locators.card_expiry
    cvv = locators.cvc
    zip_code = locators.zip_code
    checkbox = locators.checkbox
    mobile_num = locators.mobile_no
    pay_button = locators.pay_button
    checkout_heading = locators.checkout_heading
    sunscreen_heading = locators.heading_sunscreen
    moisturizers_heading = locators.heading_moisturizer    
    product_category = []    
    product_moisturizers_category = []
    product_sunscreens_category = []
    pay_with_card_button = locators.pay_with_card
    

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
        result_flag &= self.check_redirect_cart()

        return result_flag

    def select_product_type(self,product_moisturizers_category,product_sunscreens_category):
        "Select products type"          
        result_flag = None
        if 'sunscreen' in self.get_current_url():
            result_flag = self.process_selected_products(product_sunscreens_category)            
        else:           
            result_flag = self.process_selected_products(product_moisturizers_category)  ## changed sunscreens to moisturizers            
        
        return result_flag 

    def check_redirect_cart(self):
        "check if we have been redirected to the cart page"
        result_flag = False
        if 'cart' in self.get_current_url():
            result_flag = self.click_element(self.pay_with_card_button) 
            self.switch_frame(self.iframe_name)
            result_flag &= self.pay_process()
            
        return result_flag

    def random_email(self):
        "getting random mail everytime"
        random_num = random.randint(1,1000)
        random_mail = 'Qxf2' + str(random_num) + '@gmail.com'

        return random_mail
    
    def pay_process(self):
        "Filling the frame"
        result_flag = False

        result_flag =  self.set_text(self.email,self.random_email())
        result_flag &= self.set_text(self.card_number,'4242424242424242')
        result_flag &= self.set_text(self.card_expiry,'06/33')
        result_flag &= self.set_text(self.cvv,'951')
        result_flag &= self.set_text(self.zip_code,'585103')
        result_flag &= self.select_checkbox(self.checkbox)
        result_flag &= self.set_text(self.mobile_num,'7892777777')
        result_flag &= self.click_element(self.pay_button)
        time.sleep(5)
        self.switch_page('confirmation')

        return result_flag