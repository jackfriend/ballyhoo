from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Driver():
    """
    We will open up a browser that has autofilled
    credit card info, etc
    """

    def __init__(self, url):
        self.Browser = webdriver.Chrome()
        self.Browser.get(url)
        
    def add_to_cart(self, button_xpath, options):
        """
        add to cart
        """
        button = WebDriverWait(self.Browser, 20).until(
            EC.presence_of_element_located((By.XPATH, button_xpath))) 
        for option in options:      # options = [{xpath: "XPATH", index: "INDEX}...]
            select = Select(self.Browser.find_element_by_xpath(option["xpath"]))
            select.select_by_index(option["index"])
        button.click()

    def fill_form(self, input_name, fill_with):
        """
        fill a form
        """
        element = self.Browser.find_element_by_name(input_name)
        element.send_keys(fill_with)


    def select_by_name(self, input_name, index):
        """
        select elements for the form
        """
        select = Select(self.Browser.find_element_by_name(input_name))
        select.select_by_index(index)


    def process_payment(self, checkout, button_xpath, cc_info):
        """
        process the payments
        """
        self.Browser.get(checkout)        
        button = WebDriverWait(self.Browser, 10).until(
           EC.presence_of_element_located((By.XPATH, button_xpath))) 

        self.fill_form("order[billing_name]", cc_info.NAME)
        self.fill_form("order[email]", cc_info.EMAIL)
        self.fill_form("order[tel]", cc_info.TEL)
        self.fill_form("order[billing_address]", cc_info.ADDRESS)
        self.fill_form("order[billing_address_2]", cc_info.ADDRESS_2)
        self.fill_form("order[billing_zip]", cc_info.ZIP)
        self.fill_form("order[billing_city]", cc_info.CITY)
        self.select_by_name("order[billing_state]", cc_info.STATE)
        self.select_by_name("order[billing_country]", cc_info.COUNTRY)
        self.fill_form("riearmxa", cc_info.CC_NO)
        self.select_by_name("credit_card[month]", cc_info.CC_MONTH)
        self.select_by_name("credit_card[year]", cc_info.CC_YEAR)
        self.fill_form("credit_card[meknk]", cc_info.CCV)
    

        # button.click()

