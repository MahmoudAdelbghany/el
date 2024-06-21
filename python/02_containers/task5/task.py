import requests
from pprint import pprint
response = requests.get('https://api.ipify.org/?format=json')
# print(response.json())

ip = response.json()['ip']

response = requests.get('https://ipinfo.io/'+ip+'/geo')

pprint(response.json())

