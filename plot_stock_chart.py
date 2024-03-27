import pandas as pd
import matplotlib.pyplot as plt

# Charger les données
file_path = 'boeing_2019_2024_stock_price.csv'
data = pd.read_csv(file_path)

# Convertir la colonne 'Date' en type datetime pour mieux gérer les dates sur l'axe des abscisses
data['Date'] = pd.to_datetime(data['Date'])

# Créer le graphique
plt.figure(figsize=(10, 6))  # Définit la taille du graphique
plt.plot(data['Date'], data['Open'], marker='o', linestyle='-', color='b')  # Tracer le prix d'ouverture en fonction du temps

plt.title('Prix d\'ouverture des actions de Boeing (2019-2024)')  # Titre du graphique
plt.xlabel('Date')  # Étiquette de l'axe des abscisses
plt.ylabel('Prix d\'ouverture ($)')  # Étiquette de l'axe des ordonnées
plt.xticks(rotation=45)  # Rotation des étiquettes de date pour une meilleure lisibilité
plt.tight_layout()  # Ajuste automatiquement les paramètres du subplot pour qu'ils rentrent dans la zone du graphique

# Afficher le graphique
plt.show()
