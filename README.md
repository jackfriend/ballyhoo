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
	"STATE": 0, 		# index
	"COUNTRY": 0, 		# index
	"CC_NO": "",
	"CC_MONTH": 11,		# index
	"CC_YEAR": 3, 		# index
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
	"SIZE": 0, 		# Index
	"QUANTITY": 0, 		# Index

}
```
