import requests
from lxml import html


headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

url = "https://health-diet.ru"
response = requests.get(url + "/base_of_food/food_24529", headers=headers)

if response.status_code == 200:
    tree = html.fromstring(response.text)
    