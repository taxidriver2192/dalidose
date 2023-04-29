import requests

api_key = "H6kiaHNQrzP8YVhjILHDYvgQowhxfMbzVjUP3zUs"
headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get("https://api.printful.com/store/products", headers=headers)

if response.status_code == 200:
    data = response.json()
    print("Success:", data)
else:
    print("Error:", response.status_code, response.text)
