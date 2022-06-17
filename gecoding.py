import requests

# Base Url for geocoding
url = "https://us1.locationiq.com/v1/search.php"

address = input("Input the address: ")


private_token = "pk.7519b33c3300b85c7f98b663c9c46596"

data = {
    'key': private_token,
    'q': address,
    'format': 'json'
}

response = requests.get(url, params=data)

latitude = response.json()[0]['lat']
longitude = response.json()[0]['lon']

print(f"The latitude of the given address is: {latitude}")
print(f"The longitude of the given address is: {longitude}")
