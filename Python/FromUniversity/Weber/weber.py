import requests, sys
from bs4 import BeautifulSoup
def takepage(link = sys.argv[1]):
    r = requests.get("https://{}".format(link))
    s = BeautifulSoup(r.content)
    return s.prettify()    
