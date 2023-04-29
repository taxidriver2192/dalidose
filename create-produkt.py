import requests
import json

api_key = "H6kiaHNQrzP8YVhjILHDYvgQowhxfMbzVjUP3zUs"
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

image_url = "https://ibb.co/86L76cb"

data = {
    "sync_product": {
        "name": "New Product",
        "thumbnail": image_url
    },
    "sync_variants": [
        {
            "retail_price": "21.00",
            "variant_id": 4011,
            "files": [
                {
                    "url": image_url
                },
                {
                    "type": "back",
                    "url": image_url
                }
            ]
        },
        {
            "retail_price": "21.00",
            "variant_id": 4012,
            "files": [
                {
                    "url": image_url
                },
                {
                    "type": "back",
                    "url": image_url
                }
            ]
        }
    ]
}

response = requests.post("https://api.printful.com/store/products", headers=headers, data=json.dumps(data))

if response.status_code == 200:
    result = response.json()
    print("Success:", result)
else:
    print("Error:", response.status_code, response.text)
