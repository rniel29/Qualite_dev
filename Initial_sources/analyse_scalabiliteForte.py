import pandas as pd
import matplotlib.pyplot as plt
import os

# Lire le fichier CSV (dans le dossier parent)
csv_path = os.path.join( 'resultat', 'resultats.csv')

if not os.path.exists(csv_path):
    print(f"Erreur: Le fichier {csv_path} n'existe pas.")
    print("Veuillez d'abord exécuter le programme Java pour générer des résultats.")
    exit(1)

# Charger les données
df = pd.read_csv(csv_path)

# Afficher les données chargées
print("Données chargées:")
print(df)
print()

# Grouper par nombre de workers et prendre le temps moyen si plusieurs mesures
grouped = df.groupby('NumWorkers')['Temps(ns)'].median().reset_index()
grouped = grouped.sort_values('NumWorkers')

print("Temps médians par nombre de workers:")
print(grouped)
print()

# Trouver le temps de référence (avec 1 worker)
if 1 in grouped['NumWorkers'].values:
    T1 = grouped[grouped['NumWorkers'] == 1]['Temps(ns)'].values[0]
else:
    print("Attention: Pas de mesure avec 1 worker. Utilisation du minimum comme référence.")
    T1 = grouped['Temps(ns)'].min()

print(f"Temps de référence T1: {T1} ns")
print()

# Calculer le speedup Sp = T1 / Tp
grouped['Speedup'] = T1 / grouped['Temps(ns)']

print("Speedup calculé:")
print(grouped)
print()

# Créer le graphique
plt.figure(figsize=(10, 6))

# Tracer le speedup réel
plt.plot(grouped['NumWorkers'], grouped['Speedup'], 'o-', 
         label='Speedup réel', linewidth=2, markersize=8)

# Tracer le speedup idéal (linéaire)
max_workers = grouped['NumWorkers'].max()
plt.plot([1, max_workers], [1, max_workers], '--', 
         label='Speedup idéal (linéaire)', color='gray', linewidth=1.5)

plt.xlabel('Nombre de processus (P)', fontsize=12)
plt.ylabel('Speedup (Sp = T1/Tp)', fontsize=12)
plt.title('Scalabilité du calcul de Pi (Monte Carlo)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)

# Sauvegarder le graphique
output_path = os.path.join( 'resultat', 'scalabilite.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Graphique sauvegardé dans {output_path}")

# Afficher le graphique
plt.show()

# Calculer l'efficacité
grouped['Efficacite'] = (grouped['Speedup'] / grouped['NumWorkers']) * 100

print("\nAnalyse de l'efficacité:")
print(grouped[['NumWorkers', 'Speedup', 'Efficacite','Temps(ns)']])
