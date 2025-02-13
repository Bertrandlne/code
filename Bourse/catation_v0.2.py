#!/usr/bin/env python3  

import yfinance as yf 
import pandas as pd 
import time

# Définir les symboles des tickers
TICKERS = ["^FCHI", "ORA.PA", "TTE.PA", "TEP.PA", "0NQT.IL", "PAEEM.PA", "VLA.PA", "0P00000JQ4.F", "UBI.PA" ]

# Définir les noms de colonnes
COLUMNS = ['Nom de l\'action', 'Cours actuel', 'Variation (%)', 'Cours à l\'ouverture',
            'Plus haut de la journée', 'Plus bas de la journée', 'Cours de clôture de la veille',
            'Secteur d\'activité']

# Définir le nombre d'itérations souhaité
NUM_ITERATIONS = 10

# Définir le délai entre les itérations en secondes
DELAY = 30

def get_ticker_data(ticker_symbol):
    """
    Récupère les données pour un symbole de ticker spécifique
    """
    ticker_data = yf.Ticker(ticker_symbol)
    ticker_history = ticker_data.history(period="1mo", interval="1d")
    current_price = ticker_history['Close'].iloc[-1]
    open_price = ticker_history['Open'].iloc[-1]
    high_price = ticker_history['High'].iloc[-1]
    low_price = ticker_history['Low'].iloc[-1]
    previous_close_price = ticker_history['Close'].iloc[-2]
    variation = (current_price - previous_close_price) / previous_close_price * 100
    sector = ticker_data.info.get('sector', 'N/A')
    name = ticker_data.info.get('longName', 'N/A')
    return [name, current_price, variation, open_price, high_price, low_price, previous_close_price, sector]

# Initialiser un DataFrame vide pour stocker les données
data = pd.DataFrame(columns=COLUMNS)

# Initialiser le compteur d'itérations
iteration_count = 0

while True:
    # Obtenir les données pour chaque ticker
    for ticker_symbol in TICKERS:
        try:
            ticker_data = get_ticker_data(ticker_symbol)
            data.loc[ticker_symbol] = ticker_data
        except Exception as e:
            print(f"Erreur lors de la récupération des données pour {ticker_symbol}: {e}")

    # Convertir les données numériques en nombres flottants avec trois décimales et remplacer les points par des virgules
    data[['Cours actuel', 'Cours à l\'ouverture', 'Plus haut de la journée', 'Plus bas de la journée', 'Cours de clôture de la veille', 'Variation (%)']] = data[['Cours actuel', 'Cours à l\'ouverture', 'Plus haut de la journée', 'Plus bas de la journée', 'Cours de clôture de la veille', 'Variation (%)']].astype(float).round(3).map(lambda x: str(x).replace('.', ','))

    # Enregistrer les données dans un fichier CSV
    data.to_csv('C:\\Users\\adber\\OneDrive\\Banque\\cours_actions.csv')

    # Incrémenter le compteur d'itérations
    iteration_count += 1

    # Vérifier si le nombre d'itérations souhaité a été atteint
    if iteration_count >= NUM_ITERATIONS:
        break

    # Attendre avant de récupérer les données à nouveau
    time.sleep(DELAY)
