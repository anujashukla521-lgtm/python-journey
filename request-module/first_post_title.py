import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("Status code:",response.status_code)

response.raise_for_status()

data = response.json()
print("Title:",data[0]["title"])