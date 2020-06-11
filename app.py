from supreme import *
from browser import *
from utils import *
import config
import time


# 1) Wait until items are available
# 2) Create the Supreme shop object
# 3) search for the specified item
# 4) create the specifed item and place in the Order var
the_delay("https://www.supremenewyork.com/mobile_stock.json", config.ITEM["NAME"])
shop = Supreme()
order_url = shop.get_url(config.ITEM["POSITION"])
Order = Item("https://www.supremenewyork.com", order_url)

# 5) open webbrowser to the Order's href
webpage = Driver(Order.href)

options = [
        {"xpath": config.BUTTONS["SIZE"]}
         # "index" : config.ITEM["SIZE"]}
#        {"xpath": config.BUTTONS["QUANTITY"],
#         "index": config.ITEM["QUANTITY"]}
]

# 6) Select size
# 7) wait half a second
# 8) proceed to checkout and fill out all forms
# CHECKOUT is not pressed by default. You need to manually press checkout
# To completely automate, uncomment button.click() in browser.py > Browser() > process_payment()
webpage.add_to_cart(config.BUTTONS["ADD_TO_CART"], options)
time.sleep(0.5)
webpage.process_payment("https://www.supremenewyork.com/checkout", config.BUTTONS["CHECKOUT"], config.CC_INFO)
