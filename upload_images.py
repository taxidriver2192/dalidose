import os
import requests

api_key = "H6kiaHNQrzP8YVhjILHDYvgQowhxfMbzVjUP3zUs"
headers = {
    "Authorization": f"Bearer {api_key}",
}

file_path = "./images/1.jpg"

with open(file_path, "rb") as image_file:
    files = {"files[]": image_file}
    response = requests.post("https://api.printful.com/files/upload", headers=headers, files=files)

if response.status_code == 200:
    result = response.json()
    print("Success:", result)
else:
    print("Error:", response.status_code, response.text)
