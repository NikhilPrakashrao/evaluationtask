#Common locator file for all locators
#Locators are ordered alphabetically

############################################
#Selectors we can use
#ID
#NAME
#css selector
#CLASS_NAME
#LINK_TEXT
#PARTIAL_LINK_TEXT
#XPATH
###########################################

#Main page
temp_field = "xpath,//span[@id ='temperature']"
click_moisturizers = "xpath,//button[text()='Buy moisturizers']" ##added space between Buy_moisturizers
click_sunscreens= "xpath,//button[text()='Buy sunscreens']" ##added space between Buy_sunscreens

#Moisturizer header
heading_moisturizer = "xpath,//h2[contains(text(),'Moisturizers')]"

#Sunscreen header
heading_sunscreen = "xpath,//h2[contains(text(),'Sunscreens')]"

page_title = "xpath,//h2"

#moisturizers = "xpath,//div[contains(@class,'text-center col-4')]"
#sunscreens = "xpath,//div[contains(@class,'text-center col-4')]"

# get product names
moisturizers_names = "xpath,//p[contains(@class,'font-weight-bold top-space-10')]"
sunscreens_names ="xpath,//p[contains(@class,'font-weight-bold top-space-10')]"

#get product price
moisturizers_price = "xpath,//p[contains(text(),'Price')]"
sunscreens_price = "xpath,//p[contains(text(),'Price')]"

product_price_element = "xpath,//p[contains(text(), '%s')]/following-sibling::p"
product_add_element ="xpath,//p[contains(text(), '%s')]/following-sibling::p[contains(text(),'%s')]/following-sibling::button"


# click cart button
click_cart = "xpath,//button[contains(@class,'nav-link')]"
checkout_heading = "xpath,//h2"

# Click pay with card button
pay_with_card = "xpath,//button['Pay with Card']"

# get stripe iframe name
iframe_name = "//iframe[@name='stripe_checkout_app']"

#Stripe Payment gateway
email = "xpath,//input[@type='email']"       

card_number  =  "xpath,//input[@type='tel']"

card_expiry = "xpath,//input[@placeholder='MM / YY']"

cvc = "xpath,//input[@placeholder='CVC']"

zip_code = "xpath, //input[@placeholder='ZIP Code']"

checkbox = "xpath,//div[contains(@class,'Checkbox-tick')]" ## added by me

mobile_no = "xpath,//input[contains(@autocomplete,'mobile tel')]" ## added by me

pay_button = "xpath, //button[@type ='submit']"







