import requests, json
site = requests.get("https://api.exchangeratesapi.io/latest")
data = json.loads(site.text)
print(data["rates"]["TRY"])