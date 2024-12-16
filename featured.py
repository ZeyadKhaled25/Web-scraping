import requests
from bs4 import BeautifulSoup
import csv
import json


url = 'https://www.baraasallout.com/test.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

featured_products = []
products = soup.find_all('div', class_='featured-product')

for product in products:
    product_id = product['data-id']
    name = product.find('span', class_='name').get_text()
    price = product.find('span', class_='price', style='display: none;').get_text()
    colors = product.find('span', class_='colors').get_text()
    featured_products.append({
        'id': product_id,
        'name': name,
        'price': price,
        'colors': colors
    })
print(featured_products)