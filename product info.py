
import requests
from bs4 import BeautifulSoup
import csv
import json

url = 'https://www.baraasallout.com/test.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


cards = soup.find_all('div', class_='card')
products = []

for card in cards:
    title = card.find('h3').get_text()
    price = card.find('span', class_='price').get_text()
    stock = card.find('span', class_='stock').get_text()
    button_text = card.find('button').get_text()
    products.append({
        'Book Title': title,
        'Price': price,
        'Stock Availability': stock,
        'Button Text': button_text
    })

print(products)
with open('Product_Information.json', 'w', encoding='utf-8') as file:
    json.dump(products, file, ensure_ascii=False, indent=4)
