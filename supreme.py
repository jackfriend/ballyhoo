from http_requests import *
import bs4 as BS
import json as JSON


class Supreme():
    """
    This class represents the Supreme website
    """
    
    def __init__(self):
        self.shop_url = "https://www.supremenewyork.com/shop/all"

    def get_url(self, pos):
        """
        Pass in where the item is located (Pos, int) where pos is an index starting at 0
        return relative url
        """
        full_shop = http_get(self.shop_url)
        soup = BS.BeautifulSoup(full_shop, 'html.parser')
        soup_div = soup.body.findAll("div")     # BS.finaAll() returns a list; make sure to choose the first object of this list
        soup_ul = soup_div[1].findAll("ul")[2]  # BS.findAll() returns a list; select the 3 (index=2) ul
        soup_li = soup_ul.findAll("li")[pos]    # select the specified position
        soup_a = soup_li.div.a
        soup_rel_href = soup_a['href']
        return soup_rel_href




class Item():
    """
    This is the specific item we want
    """
    
    def __init__(self, static_url, rel_href):
        self.static_url = static_url
        self.rel_href = rel_href
        self.href = self.static_url + self.rel_href
        self.href_json = self.href + '.json'




