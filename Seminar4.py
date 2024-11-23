import requests
from lxml import html



headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

url = 'https://health-diet.ru'
response = requests.get(url + "/base_of_food/food_24529", headers=headers)
print(response.status_code)
# dom = html.fromstring(response.text)

# names = dom.xpath("//h3[contains(@class, 'textual-display')]")
# print(names)