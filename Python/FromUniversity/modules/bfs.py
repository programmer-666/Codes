from bs4 import BeautifulSoup
import requests

s = BeautifulSoup(requests.get("https://www.youtube.com/watch?v=H4j0Q0iGkdY&list=PLuXQ-zV50qtiGM7U9blPhFH8r1CGivacb").text, 'html.parser')
#sp = s.prettify()
#print(s.title, s.title.name, s.title.string)
#print(s.find_all('div')[10].iframe)
#print(s.ul.findChildren())
#print(s.div.find_next_sibling())#kardeş
for l in s.find_all("a"):
    print(l.get('href'))