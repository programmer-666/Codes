import requests
cookie = {"Cookie": "_ga=GA1.2.1907798292.1587690849; RTConsent=1111; __gads=ID=9a42666f84eaf72e:T=1591187409:S=ALNI_MbseJ8Zu0CDLiJOpCrAj6iioMPV7A"}

with open("fuzzwords.txt") as fl:
    cont = fl.read()

for i in cont.split("\n"):
    url = "https://www.rapidtables.com/convert/number/"+str(i)
    gt = requests.get(url = url, headers = cookie)

    if "200" in str(gt.status_code):
        print(i, "Found")
