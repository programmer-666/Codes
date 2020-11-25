import requests 
import json

rq = requests.get("https://suhaarslan.com/java-koleksiyonlar-hashset/")
print(rq.text)