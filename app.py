from supreme import *
from browser import *
import config
import time



shop = Supreme()
shirt_location = shop.get_url(config.ITEM["POSITION"])

Shirt = Item("https://www.supremenewyork.com", shirt_location)


webpage = Driver(Shirt.href)


options = [
        {"xpath": config.BUTTONS["SIZE"],
          "index" : config.ITEM["SIZE"]}
#        {"xpath": config.BUTTONS["QUANTITY"],
#         "index": config.ITEM["QUANTITY"]}
]

webpage.add_to_cart(config.BUTTONS["ADD_TO_CART"], options)
time.sleep(0.5)
webpage.process_payment("https://www.supremenewyork.com/checkout", config.BUTTONS["CHECKOUT"], config.CC_INFO)
