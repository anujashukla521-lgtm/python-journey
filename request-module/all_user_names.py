import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

response.raise_for_status()
data = response.json()

for index,name in enumerate(data):
    print(data[index]["name"])