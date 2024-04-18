import requests

response = requests.get("https://restcountries.com/v3.1/all")

if response.status_code == 200:
    data = response.json()
    print(data)
    print("Data recieved successfully")

else:
    print("status 400")
    