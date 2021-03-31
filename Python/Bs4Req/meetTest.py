import requests
from bs4 import BeautifulSoup

r = requests.get('https://meet.google.com/vjd-zeuf-ahs')
soup = BeautifulSoup(r.content, 'lxml')
with open('r.htm', 'w') as f:
    f.write(soup.prettify())