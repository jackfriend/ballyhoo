from supreme import *


shop = Supreme()
jacket_location = shop.get_url(0)

jacket = Item("https://www.supremenewyork.com", jacket_location)
print(jacket.href)
