import json 
d = '{"name":"x","v":1}'
js = json.loads(d)#dict to js
print(js)
jsd = json.dumps(json.loads(d))#jsn to dict
print(jsd)
#dosya işlemlerinde dump ve load