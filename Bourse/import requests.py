import requests
from bs4 import BeautifulSoup

def extract_data(url):
    response = requests.get(url)
    response.raise_for_status()  # Vérifie si la requête a réussi
    return response.content

def get_stock_info(soup):
    # Essayer de trouver le nom de l'action
    name_tag = soup.find('h1')  # Vous devrez peut-être ajuster ce sélecteur
    name = name_tag.get_text(strip=True) if name_tag else 'Nom non trouvé'

    # Essayer de trouver le prix actuel
    price_tag = soup.find('span', class_='price')  # Ajuster ce sélecteur
    price = price_tag.get_text(strip=True) if price_tag else 'Prix non trouvé'

    # Essayer de trouver la variation du prix
    variation_tag = soup.find('span', class_='variation')  # Ajuster ce sélecteur
    variation = variation_tag.get_text(strip=True) if variation_tag else 'Variation non trouvée'

    # Essayer de trouver le volume
    volume_tag = soup.find('div', class_='volume')  # Ajuster ce sélecteur
    volume = volume_tag.get_text(strip=True) if volume_tag else 'Volume non trouvé'

    return {
        'Nom': name,
        'Prix': price,
        'Variation': variation,
        'Volume': volume
    }

if __name__ == '__main__':
    url = "https://live.euronext.com/fr/product/equities/FR0000051732-XPAR"
    html = extract_data(url)
    soup = BeautifulSoup(html, "html.parser")

    stock_info = get_stock_info(soup)
    print(stock_info)
