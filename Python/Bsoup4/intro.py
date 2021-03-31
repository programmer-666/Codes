from bs4 import BeautifulSoup
import requests
r = requests.get('https://www.producthunt.com')
source = BeautifulSoup(r.content, 'lxml')
#print(source) # içerik
#print(source.find('p')) # sayfadaki ilk değerdir, .text ile etiketler kaldırılıe
#print(source.find('p').text)
#print(source.find('p', attrs={'class':'styles_lineHeight__2RYYy'})) # bir seçiciye göre ilk etiketi bulur
#for i in source.findAll('a', attrs={'class': 'styles_lineHeight__2RYYy'}, limit=5): # bs4 result set olarak etiket ve seçiciye sahip tüm değerleri bulur
#    print(i.get('href'), i.text) # .get() ile etiketin içinden bir alana ait değer alınabilir
#print(source.find_all(string=["Sign Up","Log In"])) # sign/login up stringlerini arar, bulursa gösterir
#print(source.findAll('span', string='Subscribe')) # span etiketine sahip subscribe textini arar, bulursa döndürür
#print(source.find("ul",attrs={"class":"list_0372b"}).li.text) # ul içindeki ilk etiketin değeri
#print(source.find("ul",attrs={"class":"list_0372b"}).li.next_sibling.text) # ul içindeki ilk etiketten sonraki etiketin değeri, previus_sibling öncesi
#next_siblings, previus_siblings değerleri ise çoklu değer döndürür
#for i in source.find('div').select('li:nth-of-type(3)'): # css selectorle de seçilebilir
#    print(i.text)
#print(source.select("html > body > div > div > main > div > div > div > div > span")) # a:nth-of-type(2) # bir yöntem
#print(source.select("p.text_44214")) # text_44214 sınıflı p etiketi
#print(source.select('a[href="/ship"]')) # a içinde href alanında /ship değeri olan etiketler
#for i in source.select('a[href^="/topics/t"]'):
#    print(i.text)

### modifiye ###
#print(source.find('a', attrs={'class': 'styles_lineHeight__2RYYy'})['class'])
#source.find('a', attrs={'class': 'styles_lineHeight__2RYYy'})['class'] = [1,2]
#print(source.find('span', string='Subscribe').string)
#source.find('span', string='Subscribe').string = 'test'
#print(source.find('span', string='test').string) # .append(str) ile değer eklenir

# çıktı format
print(source.find('span').prettify()) # kodları okunabilir yapar
source.encode('utf-8')
