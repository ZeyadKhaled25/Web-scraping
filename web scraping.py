import requests
from bs4 import BeautifulSoup
import csv
import json


url = 'https://www.baraasallout.com/test.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 1. Extract Text Data: ()

headings = [heading.get_text() for heading in soup.find_all(['h1', 'h2'])]
paragraphs = [p.get_text() for p in soup.find_all('p')]
list_items = [li.get_text() for li in soup.find_all('li')]


with open('Text_Data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['*******Headings******'])
    writer.writerows([[heading] for heading in headings])
    writer.writerow(['***********Paragraphs**********'])
    writer.writerows([[paragraph] for paragraph in paragraphs])
    writer.writerow(['************List Items*******'])
    writer.writerows([[item] for item in list_items])

# 2. Extract Table Data:
table = soup.find('table')
rows = table.find_all('tr')

table_data = []
for row in rows:
    cols = row.find_all('td')
    cols = [col.get_text() for col in cols]
    table_data.append(cols)

with open('Extract_Table_Data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Product Name', 'Price', 'Stock Status'])
    writer.writerows(table_data)

# 3. Extract Product Information (Cards Section):
cards = soup.find_all('div', class_='card')
products = []

for card in cards:
    title = card.find('h3').get_text() if card.find('h3') else 'N/A'
    price = card.find('span', class_='price').get_text() if card.find('span', class_='price') else 'N/A'
    stock = card.find('span', class_='stock').get_text() if card.find('span', class_='stock') else 'N/A'
    button_text = card.find('button').get_text() if card.find('button') else 'N/A'
    products.append({
        'Book Title': title,
        'Price': price,
        'Stock Availability': stock,
        'Button Text': button_text
    })

with open('Product_Information.json', 'w', encoding='utf-8') as file:
    json.dump(products, file, ensure_ascii=False, indent=4)

# 4. Extract Form Details:
form = soup.find('form')
inputs = form.find_all('input')

form_details = []
for input_tag in inputs:
    field_name = input_tag.get('name')
    input_type = input_tag.get('type')
    default_value = input_tag.get('value', '')
    form_details.append({
        'Field Name': field_name,
        'Input Type': input_type,
        'Default Value': default_value
    })

with open('Form_Details.json', 'w', encoding='utf-8') as file:
    json.dump(form_details, file, ensure_ascii=False, indent=4)

# 5. Extract Links and Multimedia:
links = [{'href': a['href'], 'text': a.get_text()} for a in soup.find_all('a', href=True)]
videos = [{'src': iframe['src']} for iframe in soup.find_all('iframe')]

with open('Links_and_Multimedia.json', 'w', encoding='utf-8') as file:
    json.dump({'links': links, 'videos': videos}, file, ensure_ascii=False, indent=4)

# 6. Scraping Challenge(features):
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