import requests as re

def http_get(url, params={}, data={}):
    """
    Pass a url, return html (as a string?)
    """
    r = re.get(url, params={}, data=data)
    return r.text

    
