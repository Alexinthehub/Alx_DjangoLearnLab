import requests

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Here's a random joke for you:\n{data['setup']} ... {data['punchline']}")
else:
    print("Failed to fetch joke. Status code:", response.status_code)