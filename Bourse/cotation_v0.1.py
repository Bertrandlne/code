#!/usr/bin/env python3

import yfinance as yf
import pandas as pd
import time

# Définir les symboles des tickers
tickers = ["^FCHI", "ORA.PA", "TTE.PA", "TEP.PA", "0NQT.IL", "PAEEM.PA" ]

# Définir le nombre d'itérations souhaité
num_iterations = 10

# Initialiser le compteur d'itérations
iteration_count = 0

# Initialiser un DataFrame vide pour stocker les données
data = pd.DataFrame()

while True:
    # Obtenir les données pour chaque ticker
    for ticker_symbol in tickers:
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
        data.loc[ticker_symbol, 'Nom de l\'action'] = name
        data.loc[ticker_symbol, 'Cours actuel'] = current_price
        data.loc[ticker_symbol, 'Variation (%)'] = variation
        data.loc[ticker_symbol, 'Cours à l\'ouverture'] = open_price
        data.loc[ticker_symbol, 'Plus haut de la journée'] = high_price
        data.loc[ticker_symbol, 'Plus bas de la journée'] = low_price
        data.loc[ticker_symbol, 'Cours de clôture de la veille'] = previous_close_price
        data.loc[ticker_symbol, 'Secteur d\'activité'] = sector

    # Convertir les données numériques en entiers
    data[['Cours actuel', 'Cours à l\'ouverture', 'Plus haut de la journée', 'Plus bas de la journée', 'Cours de clôture de la veille', 'Variation (%)']] = data[['Cours actuel', 'Cours à l\'ouverture', 'Plus haut de la journée', 'Plus bas de la journée', 'Cours de clôture de la veille', 'Variation (%)']].astype(int)
    
    # Enregistrer les données dans un fichier CSV
    data.to_csv('C:\\Users\\adber\\OneDrive\\Banque\\cours_actions.csv', index_label='Symbole', float_format='%.3f')
   
    # Incrémenter le compteur d'itérations
    iteration_count += 1

    # Vérifier si le nombre d'itérations souhaité a été atteint
    if iteration_count >= num_iterations:
        break

       # Attendre 30 secondes avant de récupérer les données à nouveau
    time.sleep(30)
