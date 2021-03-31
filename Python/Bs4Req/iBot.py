import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.python.org/jobs')
soup = BeautifulSoup(r.content, 'lxml')

pages = soup.findAll('ul', attrs={'class':'pagination'})
pageLen = len(soup.findAll('ul', attrs={'class':'pagination'})[0].find_all('li')) # look again

for pageN in range(pageLen+1):
    pageReq = requests.get('https://www.python.org/jobs/?page='+str(pageN))
    inSoup = BeautifulSoup(pageReq.content, 'lxml')
    
    jobs = inSoup.find('div', attrs={'class':'row'})
    print(jobs, '\n')
    break