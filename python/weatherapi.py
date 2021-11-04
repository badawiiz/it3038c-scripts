import json
import requests

print('Please enter your ZIP code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=ffa423b7cea589267e93617528c53ead' % zip) 

data=r.json()

print (data['weather'][0]['description'])


