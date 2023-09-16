from requests import get
from bs4 import BeautifulSoup

response = get('https://www.saucedemo.com/')
soup = BeautifulSoup(response.content, "html.parser")
blocks = soup.findAll('div', class_='')
for block in blocks:
    print(block)
