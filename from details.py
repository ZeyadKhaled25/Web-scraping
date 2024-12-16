import requests
from bs4 import BeautifulSoup
import csv
import json

url = 'https://www.baraasallout.com/test.html'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

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