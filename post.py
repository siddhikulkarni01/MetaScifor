
import requests

result = {'name': 'xyz'}

response = requests.post("https://api.quotable.io/random", data= result)

if response.status_code == 200:
    print(response.json())
else:
    print(response.status_code)

