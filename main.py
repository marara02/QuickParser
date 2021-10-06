# import logging
#
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger('wb')
#
# import requests
# import warnings
# from urllib3.exceptions import InsecureRequestWarning
#
# warnings.simplefilter('ignore', InsecureRequestWarning)
#
# proxyDict = {
#     "http": "http://3.21.177.144:80"
# }
#
# headers = {
#     'Host': "2gis.kz",
#     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
#     'Accept': '*/*',
#     'Accept-Encoding': 'gzip, deflate, br',
#     'Connection': 'keep-alive'
# }
#
# url = "https://kingfisher.kz/moreprodukty/krevetki/"
# req = requests.get(url=url, verify=False)
# src = req.text
# print(src)

import requests
from bs4 import BeautifulSoup
import json

# url = "https://kingfisher.kz/moreprodukty/krevetki/"
#
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
#
# req = requests.get(url, headers=headers)
# src = req.text
#
# with open("main.html", "w", encoding="utf-8") as file:
#     file.write(src)

# with open("main.html", encoding="utf-8") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, 'lxml')
# all_blocks = soup.find_all(class_="goodsBlock")
#
# all_goods = {}
# for good in all_blocks:
#     item_href = good.find("a")
#     item_url = "https://kingfisher.kz" + item_href.get("href")
#     item_text = good.text
#     all_goods[item_text] = item_url
#
# with open('goods.json', "w", encoding="utf-8") as file:
#     json.dump(all_goods, file, indent=4)

with open("goods.json", encoding="utf-8") as file:
    all_goods = json.load(file)

count = 0
total_product_crev = []
for text, url in all_goods.items():
    if count == 0:
        req = requests.get(url=url, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "lxml")

        product_name = soup.find("h1")
        product_cost = soup.find(class_="gPrice")
        product_city = soup.find(class_="popupBtn_city")

        total_product_crev.append({
            "product name": product_name.text,
            "product cost": product_cost.text,
            "product city": product_city.text

        })
with open("part_sea.json", "a", encoding="utf-8") as file:
    json.dump(total_product_crev, file, indent=4, ensure_ascii=False)
