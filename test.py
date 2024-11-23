import requests

headers = {
       "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
   }
url = "https://www.ebay.com/b/Fishing-Equipment-Supplies/1492/bn_1851047"
response = requests.get(url, headers=headers)
print(response.status_code)