import requests
from bs4 import BeautifulSoup
import csv


url = 'https://www.baraasallout.com/test.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


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