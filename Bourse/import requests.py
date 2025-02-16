import requests
from bs4 import BeautifulSoup

url = "https://live.euronext.com/fr/product/equities/FR0000133308-XPAR"

x = requests.get(url)
soup = BeautifulSoup(x.text, "html.parser")

print(soup.title)
