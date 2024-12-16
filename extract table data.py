import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.baraasallout.com/test.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

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