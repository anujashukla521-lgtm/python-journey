import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

response.raise_for_status()
data = response.json()

username = input("Enter username: ")

found = False
for user in data:
    if username.lower() == user["name"].lower():
        found = True
        print("Name:",user["name"])
        print("Email:",user["email"])
        print("Company:",user["company"]["name"])
        print("City:",user["address"]["city"])
        print()
        break
    
if not found:
    print("User not found")
