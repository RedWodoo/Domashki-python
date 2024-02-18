"""
program
"""
from bs4 import BeautifulSoup
import requests
GET_URL = 'https://yandex.kz/pogoda/astana'
response = requests.get(GET_URL)
soup = BeautifulSoup(response.text,'html.parser')
tmp = soup.find('span',class_='temp__value temp__value_with-unit').text
print(tmp + '°C')
