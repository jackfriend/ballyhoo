# Ballyhoo

Selenium Autocheckout for the supreme NY website.

button.click() is commented out by default. Make sure you have the right item during checkout.
Enabling button.click() risks having the wrong item during checkout.

## Config.py
The config.py is in the .gitignore. It holds the pribate information (i.e. Credit Card info.)
Copy and paste this into a new config.py

```
CC_INFO = {
	"NAME": "",
	"EMAIL": "",
	"TEL": "",
	"ADDRESS": "",
	"ADDRESS_2": "",
	"ZIP": "",
	"CITY": "",
	"STATE": 0, 		  # index (NY = 36)
	"COUNTRY": 0, 		# index (USA = 0)
	"CC_NO": "1111 2222 3333 4444", # spaces necessary
	"CC_MONTH": 0,		# index (01=0, 02=1, 03=2...)
	"CC_YEAR": 0, 		# index (2020=0, 2021=1, 2022=2...)
	"CVV": ""
}


BUTTONS = {
	"CHECKOUT": "/html/body/div[2]/div[1]/form/div[3]/div[2]/input",
	"ADD_TO_CART": "/html/body/div[2]/div/div[2]/div/form/fieldset[3]/input"
	"SIZE": "/html/body/div[2]/div/div[2]/div/form/fieldset[1]/select",
	"QUANTITY: "/html/body/div[2]/div/div[2]/div/form/fieldset[2]/select"
}

ITEM = {
	"POSITION": 0		# Index
	"SIZE": "", 		# Small, Medium, Large, X-Large. Get these values from the UK site
	"QUANTITY": 0, 		# Index (Best to leave at quanity 1, index=0)

}
```
