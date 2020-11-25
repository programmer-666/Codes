import os
import time
print(os.getcwd())#Mevcut Dizin
os.mkdir("TheDirectory")#klasör yaratma
time.sleep(0.4)
os.rmdir("TheDirectory")#k silme varsa alt klasör removedirs
#os.chdir('/mnt/e/CodeStorage/Python3/')#dizin değiştirme
print(os.getcwd())
#os.makedirs("test/1")
print(os.listdir("../"))
print(os.stat("OpS.py").st_size, os.stat("OpS.py").st_ctime, os.stat("OpS.py").st_atime, os.stat("OpS.py").st_mtime)#byte cinsinden boyut oluşturulma zamanı son erişim zamanı son değiştirilme tarihi
os.system("echo hi")
os.rename("s.py", "show.py")
os.rename("show.py", "s.py")
print(os.path.abspath("OpS.py"))#dosyanın tam yolunu döndürür
print(os.path.dirname(os.path.abspath("OpS.py")))#dosyanın dizin ismi/bulunduğu isim
print(os.path.exists("OpS.py"))#var mı yok mu
print(os.path.isdir(os.path.dirname(os.path.abspath("OpS.py"))))#isfile dosya için olan
print(os.path.join("c:", "test"))#birleştirme
print(os.path.split(os.path.dirname(os.path.abspath("OpS.py"))))#ayırma
print(os.path.splitext (os.path.dirname(os.path.abspath("OpS.py"))))#isme göre