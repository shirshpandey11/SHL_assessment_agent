import requests

url = "https://tcp-us-prod-rnd.shl.com/voiceRater/shl-ai-hiring/shl_product_catalog.json"

response = requests.get(url, timeout=30)

print("Status Code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Content Length:", len(response.content))

print("\nFirst 300 characters:\n")
print(response.text[:300])

with open("app/catalog/shl_catalog.json", "wb") as f:
    f.write(response.content)

print("\nSaved!")