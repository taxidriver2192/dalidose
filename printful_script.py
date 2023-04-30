import requests
import json

# Replace {your_token} with your actual Printful API token
api_token = "H6kiaHNQrzP8YVhjILHDYvgQowhxfMbzVjUP3zUs"
headers = {
    "Authorization": f"Bearer {api_token}",
    "Content-Type": "application/json"
}

# Function to get the products in your store
def get_store_products():
    response = requests.get("https://api.printful.com/store/products", headers=headers)
    print(json.dumps(response.json(), indent=2))

# Function to add a new product to your store
def add_new_product():
    payload = {
        "sync_product": {
            "name": "Framed Landscape Poster"
        },
        "sync_variants": [
            {
                "variant_id": 10760,
                "files": [
                    {
                        # Erstat eksempel-URL'en med din faktiske Imgur-billede-URL
                        "url": "https://i.imgur.com/fVISju4.jpeg"
                    }
                ]
            }
        ]
    }
    response = requests.post("https://api.printful.com/store/products", headers=headers, json=payload)
    print(json.dumps(response.json(), indent=2))

# Main function to call the other functions
def main():
    print("Adding a new product to the store...")
    add_new_product()

    print("\nGetting store products...")
    get_store_products()

# Call the main function
if __name__ == "__main__":
    main()
