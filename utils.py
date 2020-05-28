import requests as re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def http_get(url, params={}, data={}):
    """
    Pass a url, return html (as a string?)
    """
    r = re.get(url, params={}, data=data)
    return r.text


def the_delay(url, look_for):
    """
    Delay with a while loop until mobile_stock.json is updated
    """

    i = True
    while i:
        r = re.get(url) # get the new request (the mobile endpoint)
        r = r.json() # decode to json

        # if the item is found at the mobile endpoint
        if r["products_and_categories"]["new"][0]["name"] == look_for:
            print(look_for)
            i = False
        else:
            print(r["products_and_categories"]["new"][0]["name"])
            break


# these are helpers for the Browser class
def wait_until_clickable(browser, xpath):
    """
    wait until element in clickable
    """
    button = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath)))

    return button


def select_by_name_by_index(browser, input_name, index):
    """
    select elements for the form
    Pass an input[name=] ansd an index for option wished to by selected
    """
    select = Select(browser.find_element_by_name(input_name))
    select.select_by_index(index)


def select_by_xpath_by_text(browser, xpath, text):
    """
    select elements for the form
    Pass the Xpath of the input and the text (str) to be selected
    """
    select = Select(browser.find_element_by_xpath(xpath))
    select.select_by_visible_text(text)

def select_by_name_by_text(browser, input_name, text):
    """
    select elements for the form
    Pass the input[name=] and the visible text to select
    """
    element = browser.find_element_by_name(input_name)
    element.send_keys(text)

def select_by_classes_and_click(browser, class_name, index=0):
    """
    select elements for the form
    Pass a class name a check mark a radio box. Index defaults to 0
    """
    radios = browser.find_elements_by_class_name(class_name)
    radios[index].click()
