import requests
header = {}
u_list, p_list = ["admin"],  ["123456"]

for i in u_list:
    for j in p_list:
        url = ""+str(i)+""+str(j)
        gt = requests.get(url = url, headers = header)
        if not "incorrect" in str(gt.content):
            print("founded", i, j)
        print(" - - - ")
