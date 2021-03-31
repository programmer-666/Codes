import requests
"""
r = requests.get('https://suhaarslan.com/apix/version')
print(r) # geri dönüş 200,401,501...
print(r.content) # içerik .decode() ile dönüştürülebilir, byte olarak döner, resimlerde kullanılabilir
print(r.text) # unicode olrak içerik
print(r.status_code) # sayfa kodu, r.ok
print(r.headers) # başlık bilgileri
"""
#r = requests.get('https://suhaarslan.com/apix/imgs/sstv.jpg')
#print(r.content) # byte cinsinden resmi görüntüler
"""
r = requests.get('https://httpbin.org/get', params={'page':2, 'count':25}) # https://httpbin.org/get?page=2&count=25

print(r.text)
print(r.url) # link verir"""
"""
r = requests.post('https://httpbin.org/post', data={'username':'root', 'password':251232})
#print(r.text)
print(r.json()['form']) # dict tipinde değerleri alır"""

r = requests.get('https://httpbin.org/basic-auth/root/123', auth=('root', '123'), timeout=3) # timeout değeri saniye cinsinden
# bu işlemde ekrana username ve password isteyen bir pop up çıkıyor. auth parametresiyle belirtilen değerler
# ile giriş yapılıyor. Bilgi doğruysa username ve password geri döner, yanlışsan yanıt gelmez.
print(r.text, r.status_code)