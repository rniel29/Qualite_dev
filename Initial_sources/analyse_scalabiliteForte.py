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

# Grouper par Ntot et nombre de workers, médiane si plusieurs mesures
grouped = df.groupby(['Ntot', 'NumWorkers'])['Temps(ns)'].median().reset_index()
grouped = grouped.sort_values(['Ntot', 'NumWorkers'])

print("Temps médians par Ntot et nombre de workers:")
print(grouped)
print()

# Créer le graphique
plt.figure(figsize=(10, 6))

max_workers = grouped['NumWorkers'].max()

results = []
for ntot, group in grouped.groupby('Ntot'):
    # Trouver le temps de référence (avec 1 worker) pour ce Ntot
    if 1 in group['NumWorkers'].values:
        T1 = group[group['NumWorkers'] == 1]['Temps(ns)'].values[0]
    else:
        print(
            f"Attention: Pas de mesure avec 1 worker pour Ntot={ntot}. "
            "Utilisation du minimum comme référence."
        )
        T1 = group['Temps(ns)'].min()

    g = group.copy()
    g['Speedup'] = T1 / g['Temps(ns)']
    g['Efficacite'] = (g['Speedup'] / g['NumWorkers']) * 100
    results.append(g)

    print(f"\nSpeedup calculé pour Ntot={ntot}:")
    print(g[['NumWorkers', 'Temps(ns)', 'Speedup']])

    # Tracer une courbe par Ntot
    plt.plot(
        g['NumWorkers'],
        g['Speedup'],
        'o-',
        label=f"Ntot={ntot}",
        linewidth=2,
        markersize=6
    )

# Tracer le speedup idéal (linéaire)
plt.plot([1, max_workers], [1, max_workers], '--',
         label='Speedup idéal (linéaire)', color='gray', linewidth=1.5)

plt.xlabel('Nombre de processus (P)', fontsize=12)
plt.ylabel('Speedup (Sp = T1/Tp)', fontsize=12)
plt.title('Scalabilité forte du calcul de Pi (Monte Carlo)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend(fontsize=9)

# Sauvegarder le graphique
output_path = os.path.join('resultat', 'scalabilite_par_Ntot.png')
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Graphique sauvegardé dans {output_path}")

# Afficher le graphique
plt.show()

# Analyse de l'efficacité
result_df = pd.concat(results).sort_values(['Ntot', 'NumWorkers'])

print("\nAnalyse de l'efficacité:")
print(result_df[['Ntot', 'NumWorkers', 'Speedup', 'Efficacite', 'Temps(ns)']])
