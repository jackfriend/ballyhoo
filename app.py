from supreme import *
from browser import *
import config
import time



shop = Supreme()
shirt_location = shop.get_url(160)

Shirt = Item("https://www.supremenewyork.com", shirt_location)


webpage = Driver(Shirt.href)

options = [
        {"xpath": "/html/body/div[2]/div/div[2]/div/form/fieldset[1]/select",
          "index" : 2},
        {"xpath": "/html/body/div[2]/div/div[2]/div/form/fieldset[2]/select",
          "index": 3}
        ]

webpage.add_to_cart("/html/body/div[2]/div/div[2]/div/form/fieldset[3]/input", options)
time.sleep(5)
webpage.process_payment("https://www.supremenewyork.com/checkout", '/html/body/div[2]/div[1]/form/div[3]/div[2]/input', config.CC_INFO)
