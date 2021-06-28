import requests

response = requests.get('http://api.open-notify.org/astros.json')

#print(response.status_code)

for astronaut in response.json()['people']:
    print(astronaut['name'])

