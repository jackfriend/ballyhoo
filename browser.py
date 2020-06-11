from utils import *
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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

        button = wait_until_clickable(self.Browser, button_xpath)

        for option in options:      # options = [{xpath: "XPATH", index: "INDEX}...]
            select_by_xpath_by_text(self.Browser, option["xpath"], option["index"])

        button.click()
        print("Added to cart...")


    def process_payment(self, checkout, button_xpath, cc_info):
        """
        process the payments
        """

        self.Browser.get(checkout)
        time.sleep(0.5)
        # button = wait_until_clickable(self.Browser, button_xpath)

        select_by_name_by_text(self.Browser, "order[billing_name]", cc_info["NAME"])
        select_by_name_by_text(self.Browser, "order[email]", cc_info["EMAIL"])
        select_by_name_by_text(self.Browser, "order[tel]", cc_info["TEL"])
        select_by_name_by_text(self.Browser, "order[billing_address]", cc_info["ADDRESS"])
        select_by_name_by_text(self.Browser, "order[billing_address_2]", cc_info["ADDRESS_2"])
        select_by_name_by_text(self.Browser, "order[billing_zip]", cc_info["ZIP"])
        select_by_name_by_text(self.Browser, "order[billing_city]", cc_info["CITY"])
        select_by_name_by_index(self.Browser, "order[billing_state]", cc_info["STATE"])
        select_by_name_by_index(self.Browser, "order[billing_country]", cc_info["COUNTRY"])
        select_by_name_by_text(self.Browser, "riearmxa", cc_info["CC_NO"])
        select_by_name_by_index(self.Browser, "credit_card[month]", cc_info["CC_MONTH"])
        select_by_name_by_index(self.Browser, "credit_card[year]", cc_info["CC_YEAR"])
        select_by_name_by_text(self.Browser, "credit_card[meknk]", cc_info["CCV"])
        select_by_classes_and_click(self.Browser, "iCheck-helper", index=1) # the page has two radios; click the second radio (terms and conditions)

        # button.click()
