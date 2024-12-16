import requests
from bs4 import BeautifulSoup
import csv
import json


url = 'https://www.baraasallout.com/test.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')


links = [{'href': a['href'], 'text': a.get_text()} for a in soup.find_all('a', href=True)]
videos = [{'src': iframe['src']} for iframe in soup.find_all('iframe')]


with open('Links_and_Multimedia.json', 'w', encoding='utf-8') as file:
    json.dump({'links': links, 'videos': videos}, file, ensure_ascii=False, indent=4)