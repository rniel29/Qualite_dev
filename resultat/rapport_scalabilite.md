# Rapport de scalabilité (forte)

## Données utilisées
Fichier source : resultat/resultats.csv (médianes sur 10 exécutions par point).

## Résumé par Ntot

### Ntot = 120000
| P | Temps médian (ns) | Speedup | Efficacité |
|---:|---:|---:|---:|
| 1 | 8 651 450 | 1.00 | 100.0% |
| 2 | 10 417 050 | 0.83 | 41.5% |
| 4 | 11 029 600 | 0.78 | 19.6% |
| 8 | 9 169 050 | 0.94 | 11.8% |
| 12 | 7 640 450 | 1.13 | 9.4% |
| 24 | 7 523 800 | 1.15 | 4.8% |

**Observation :** pour un Ntot très faible, le coût fixe (overhead des threads/coordination) domine. Le speedup reste proche de 1 et l’efficacité chute rapidement.

### Ntot = 120000000
| P | Temps médian (ns) | Speedup | Efficacité |
|---:|---:|---:|---:|
| 1 | 1 583 506 500 | 1.00 | 100.0% |
| 2 | 801 236 550 | 1.98 | 98.8% |
| 4 | 416 370 650 | 3.80 | 95.1% |
| 8 | 265 156 350 | 5.97 | 74.6% |
| 12 | 202 295 600 | 7.83 | 65.2% |
| 24 | 217 065 850 | 7.30 | 30.4% |

**Observation :** très bonne scalabilité jusqu’à 4–12 workers. À 24, le speedup diminue (efficacité ~30%), suggérant saturation (coûts de synchro, contention, ou limites CPU).

### Ntot = 240000000
| P | Temps médian (ns) | Speedup | Efficacité |
|---:|---:|---:|---:|
| 1 | 3 158 829 500 | 1.00 | 100.0% |
| 2 | 1 589 188 350 | 1.99 | 99.4% |
| 4 | 820 843 300 | 3.85 | 96.2% |
| 8 | 510 256 350 | 6.19 | 77.4% |
| 12 | 380 923 750 | 8.29 | 69.1% |
| 24 | 425 297 400 | 7.43 | 30.9% |

**Observation :** comportement similaire à Ntot=120000000, avec une bonne montée jusqu’à 12 workers, puis un plafond à 24.

## Conclusion
- **Faibles Ntot** : la parallélisation n’apporte pas de gain significatif (overhead dominant).
- **Ntot élevés** : scalabilité quasi-linéaire jusqu’à 4, puis encore efficace jusqu’à 12.
- **À 24 workers** : efficacité fortement dégradée ($\approx 30\%$), indiquant une saturation des ressources ou des surcoûts de synchronisation.

## Recommandations
- Pour une **scalabilité forte**, fixer un **Ntot suffisant** (au moins 120 000 000 dans vos tests).
- Limiter le nombre de workers à **12** pour un meilleur compromis speedup/efficacité sur cette machine.
- Tester la **scalabilité faible** pour confirmer si l’efficacité se stabilise quand Ntot augmente avec P.
