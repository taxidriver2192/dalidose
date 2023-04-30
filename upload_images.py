import os
import requests

api_key = "H6kiaHNQrzP8YVhjILHDYvgQowhxfMbzVjUP3zUs"
headers = {
    "Authorization": f"Bearer {api_key}",
}

file_path = "images/1.jpg"

with open(file_path, "rb") as image_file:
    files = {"file": ("1.jpg", image_file, "image/jpeg")}
    response = requests.post("https://api.printful.com/files", headers=headers, files=files)

if response.status_code == 200:
    result = response.json()
    print("Success:", result)
else:
    print("Error:", response.status_code, response.text)
