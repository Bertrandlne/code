import requests
from bs4 import BeautifulSoup

url = "https://live.euronext.com/fr/product/equities/FR0000051732-XPAR"

x = requests.get(url)
soup = BeautifulSoup(x.text, "html.parser")

print(soup.title)
