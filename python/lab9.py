import json
import requests


r = requests.get('http://localhost:3000') 


data=r.json()

numberOfObj = len(data)

for x in range(numberOfObj):
    print(data[x]['name'] + ' is ' + data[x]['color'] + ".")




