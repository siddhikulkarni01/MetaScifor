import requests

def extract_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        print("Data extracted successfully !")
        print(response.text)
    else:
        print("Error please try again")

    return response

url = 'https://restcountries.com/v3.1/all'

print(extract_data(url))


