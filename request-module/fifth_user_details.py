import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

response.raise_for_status()

data = response.json()
print("Name:",data[4]["name"])
print("Username",data[4]["username"])
print("Email:",data[4]["email"])