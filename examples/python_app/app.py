import requests

url = "http://httpbin.org/get?message=Hello,%20World!"

print("Standard greeting:")
print("Hello, World!")
print()

print(f"Requesting: {url}")

resp = requests.get(url)

print(f"Status: {resp.status_code}")
print("JSON response:")
print(resp.json())
