import requests  

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)
response.raise_for_status()
data = response.json()

for user in data:
    print("Name:",user["name"])
    print("Company:",user["company"]["name"])
    print()