import requests
from bs4 import BeautifulSoup

r = requests.get('https://suhaarslan.com/apix/basicList')
soup = BeautifulSoup(r.content, 'lxml')
lis = soup.find('div', attrs={'class':'main_class'}).ol.find_all('li')
print(lis[0], len(lis))